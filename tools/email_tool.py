from services.integrations.email_service import EmailService
from tools.base_tool import BaseTool
from integrations.mcp.tool_response import ToolResponse


class EmailTool(BaseTool):

    def __init__(self):

        super().__init__("Email Tool")

        self.service = EmailService()

    def execute(self, tool_call):

        result = self.service.send_email(tool_call.to_email, tool_call.subject, tool_call.body)

        return ToolResponse(status = "SUCCESS", result = result)