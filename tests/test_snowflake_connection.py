from tools.database_tool import DatabaseTool

db_tool = DatabaseTool()

response = db_tool.execute(database = "snowflake", query = "SELECT * FROM EMPLOYEE")

print(response)