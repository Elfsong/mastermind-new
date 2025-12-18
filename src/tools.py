# coding: utf-8

# Author: Du Mingzhe (mingzhe@nus.edu.sg)
# Date: 2025-12-18


import subprocess
from tavily import TavilyClient
from typing import List, Dict, Any, Callable, Literal

class Tool:
    def __init__(self, name: str, description: str, func: Callable):
        self.name = name
        self.description = description
        self.func = func

    def run(self, *args: Any, **kwargs: Any) -> Any:
        return self.func(*args, **kwargs)
    
class ToolRegistry:
    def __init__(self):
        self.tools = dict()
    
    def register_tool(self, tool: Tool) -> None:
        self.tools[tool.name] = tool
    
    def get_tool(self, name: str) -> Tool:
        return self.tools[name]
    
    def get_all_tools(self) -> List[Tool]:
        return list(self.tools.values())
    
class WebSearchTool(Tool):
    def __init__(self, api_key: str):
        super().__init__(name="web_search", description="Search the web for information", func=self.search)
        self.client = TavilyClient(api_key=api_key)
    
    def search(self, query: str, max_results: int = 5, topic: Literal["general", "news", "finance"] = "general", include_raw_content: bool = False) -> str:
        """Run a web search"""
        results = self.client.search(
            query,
            max_results=max_results,
            topic=topic,
            include_raw_content=include_raw_content,
        )
        return results
    
class ExecuteCommandTool(Tool):
    def __init__(self):
        super().__init__(name="execute_command", description="Execute a command", func=self.execute)
    
    def execute(self, command: str, timeout: int = 30) -> Dict[str, Any]:
        """Execute a command"""
        try:
            result = subprocess.run(command, shell=True, capture_output=True, text=True, timeout=timeout)
            return {
                "stdout": result.stdout,
                "stderr": result.stderr,
                "returncode": result.returncode,
            }
        except subprocess.TimeoutExpired:
            return {
                "stdout": "",
                "stderr": f"Command timed out after {timeout} seconds",
                "returncode": -1,
            }
        except Exception as e:
            return {
                "stdout": "",
                "stderr": f"Error executing command: {e}",
                "returncode": -1,
            }