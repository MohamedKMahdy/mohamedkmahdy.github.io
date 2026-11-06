// Send www.mohamedkmahdy.com to the bare domain, keeping the path and query.
export async function onRequest({ request, next }) {
  const url = new URL(request.url);
  if (url.hostname === "www.mohamedkmahdy.com") {
    url.hostname = "mohamedkmahdy.com";
    return Response.redirect(url.toString(), 301);
  }
  return next();
}
