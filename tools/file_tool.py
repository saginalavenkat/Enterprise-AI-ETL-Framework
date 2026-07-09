from services.integrations.file_service import FileService
from tools.base_tool import BaseTool
from integrations.mcp.tool_response import ToolResponse


class FileTool(BaseTool):

    def __init__(self):

        super().__init__("File Tool")

        self.service = FileService()

    def execute(self, tool_call):

        action = tool_call.action

        if action == "copy":

            result = self.service.copy_file(tool_call.source, tool_call.destination)

        elif action == "move":

            result = self.service.move_file(tool_call.source, tool_call.destination)

        elif action == "delete":

            result = self.service.delete_file(tool_call.file_path)

        elif action == "read":

            result = self.service.read_text(tool_call.file_path)

        elif action == "write":

            result = self.service.write_text(tool_call.file_path, tool_call.text)

        else:

            return ToolResponse(status = "FAILED", result = "Unknown File Action")

        return ToolResponse(status = "SUCCESS", result = result)