from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import subprocess
from typing import Any, Dict, List

Fragment = Dict[str, Any]


class AemServer(BaseHTTPRequestHandler):

    def do_GET(self) -> None:
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()

        assets = self.extract_items()
        fragments = self.extract_content_fragments(assets["items"])
        response_dto = {"status": "SUCCESS", "data": {
            "fragments": fragments}, "errors": {}}
        self.wfile.write(bytes(json.dumps(response_dto), "utf-8"))

    def extract_items(self) -> Dict[str, Any]:
        pipe = subprocess.Popen(
            ["curl",
             "https://deliveryqa3.pnc.com/content/dot-pnc-aem-caas/en/mbl/remote-deposits-terms-and-conditions.model.json"],
            stdout=subprocess.PIPE)
        stdout, _ = pipe.communicate()

        obj_start = stdout.find(b'{"items":[')
        last_item = stdout.find(b'}]', obj_start)
        obj_end = stdout.find(b'}', last_item+1)
        json_data = stdout[obj_start:obj_end+1]
        assets: Dict[str, Any] = json.loads(json_data)
        return assets

    def extract_content_fragments(self, assets) -> List[Fragment]:
        return sorted([
            {
                "title": asset["elements"]["title"]["value"],
                "content": asset["elements"]["copy"]["value"],
                "fragment_id": int(asset["elements"]["fragmentId"]["value"]),
            } for asset in assets
        ], key=lambda f: f["fragment_id"])


HTTPServer(("localhost", 8000), AemServer).serve_forever()
