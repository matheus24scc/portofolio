import json, os

def build(data, out_path):
    name = data.get("name", "Meu Nome")
    bio = data.get("bio", "")
    projects = data.get("projects", [])
    links = data.get("links", {})
    items = "".join("<li><a href='%s'>%s</a></li>" % (p.get("url", ""), p.get("title", "")) for p in projects)
    link_items = "".join("<a href='%s'>%s</a> " % (u, t) for t, u in links.items())
    html = "<!doctype html><html lang='pt-BR'><head><meta charset='utf-8'><title>%s</title></head><body><h1>%s</h1><p>%s</p><h2>Projetos</h2><ul>%s</ul><p>%s</p></body></html>" % (name, name, bio, items, link_items)
    with open(out_path, "w") as f:
        f.write(html)
    return out_path

def serve(directory, port=8000):
    import http.server, socketserver
    os.chdir(directory)
    with socketserver.TCPServer(("", port), http.server.SimpleHTTPRequestHandler) as s:
        s.serve_forever()
