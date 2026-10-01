# Django on Workers

Serve a stateless Django API through Python Workers’ ASGI adapter, using URL routing and Django forms for field-level validation.

## Run locally

Install [uv](https://docs.astral.sh/uv/getting-started/installation/) and Node.js 22 or later.

```sh
npm ci
uv sync --locked
uv run pywrangler dev --config wrangler.jsonc
```

## Check and deploy

```sh
uv run pywrangler deploy --config wrangler.jsonc
```

The configuration is portable: it contains no account ID, resource ID, or maintainer custom domain. Log in with Wrangler and select your own account before deploying. Generated dependencies and build outputs stay out of source control.

## Try the example

GET /health checks liveness. GET /quote?quantity=3&unit_price_cents=250 returns a 750-cent quote. Try quantity=0, 101, a decimal, duplicate values, or missing inputs to see HTTP 400 validation errors. Both values are bounded integers (quantity 1–100; unit price 1–1000000).

This stateless Django ASGI example deliberately has no database, admin, authentication, sessions, or signed cookies. ALLOWED_HOSTS accepts public deployment hostnames and no SECRET_KEY is needed by these routes. If you add signing/auth, configure a real Worker secret; if you add the Django D1/DO database backend, follow Cloudflare’s WSGI backend guidance and its transaction limitations.

## Pattern and live demo

- [Pattern page](https://serverless.build/patterns/django-workers)
- [Live deployment](https://workers-django-python.dwarven.workers.dev)
