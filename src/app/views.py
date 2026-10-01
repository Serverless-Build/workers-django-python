from django import forms
from django.http import JsonResponse


class QuoteForm(forms.Form):
    quantity = forms.IntegerField(min_value=1, max_value=100)
    unit_price_cents = forms.IntegerField(min_value=1, max_value=1000000)


def response(data, status=200):
    return JsonResponse(data, status=status, headers={"Cache-Control": "no-store"})


def read_only(request):
    if request.method not in ("GET", "HEAD"):
        result = response({"error": "Method not allowed"}, 405)
        result["Allow"] = "GET, HEAD"
        return result


async def index(request):
    return read_only(request) or response({"framework": "Django", "adapter": "Workers ASGI", "routes": ["/health", "/quote?quantity=3&unit_price_cents=250"]})


async def health(request):
    return read_only(request) or response({"status": "ok", "marker": "SERVERLESS_BUILD_DJANGO_PYTHON_V1"})


async def quote(request):
    rejected = read_only(request)
    if rejected is not None:
        return rejected
    for name in ("quantity", "unit_price_cents"):
        values = request.GET.getlist(name)
        if len(values) != 1 or len(values[0]) > 10:
            return response({"error": "Invalid quote", "fields": {name: ["Supply exactly one bounded integer value."]}}, 400)
    form = QuoteForm(request.GET)
    if not form.is_valid():
        return response({"error": "Invalid quote", "fields": {name: [item["message"] for item in errors] for name, errors in form.errors.get_json_data().items()}}, 400)
    values = form.cleaned_data
    return response({**values, "total_cents": values["quantity"] * values["unit_price_cents"], "currency": "USD"})


def not_found(request, exception):
    return response({"error": "Not found"}, 404)


def server_error(request):
    return response({"error": "Internal server error"}, 500)
