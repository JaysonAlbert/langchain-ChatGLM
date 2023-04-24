from typing import Any, Dict, List, Union, Callable

from langchain.callbacks.base import BaseCallbackHandler
from langchain.schema import AgentFinish, AgentAction, LLMResult


class ChatBotCallbackHandler(BaseCallbackHandler):
    bot_getter: Callable

    def __init__(self, bot_getter):
        self.bot_getter = bot_getter

    def on_llm_start(self, serialized: Dict[str, Any], prompts: List[str], **kwargs: Any) -> Any:
        pass

    def on_llm_end(self, response: LLMResult, **kwargs: Any) -> Any:
        pass

    def on_llm_error(self, error: Union[Exception, KeyboardInterrupt], **kwargs: Any) -> Any:
        pass

    def on_chain_start(self, serialized: Dict[str, Any], inputs: Dict[str, Any], **kwargs: Any) -> Any:
        pass

    def on_chain_end(self, outputs: Dict[str, Any], **kwargs: Any) -> Any:
        pass

    def on_chain_error(self, error: Union[Exception, KeyboardInterrupt], **kwargs: Any) -> Any:
        pass

    def on_tool_start(self, serialized: Dict[str, Any], input_str: str, **kwargs: Any) -> Any:
        pass

    def on_tool_end(self, output: str, **kwargs: Any) -> Any:
        pass

    def on_tool_error(self, error: Union[Exception, KeyboardInterrupt], **kwargs: Any) -> Any:
        pass

    def on_text(self, text: str, **kwargs: Any) -> Any:
        value = self.bot_getter().get_config()['value']
        value.append(text, "")
        self.bot_getter().update(value=value)
        pass

    def on_agent_action(self, action: AgentAction, **kwargs: Any) -> Any:
        pass

    def on_agent_finish(self, finish: AgentFinish, **kwargs: Any) -> Any:
        pass

    def on_llm_new_token(self, token: str, **kwargs: Any) -> Any:
        value = self.bot_getter().get_config()['value']
        (text, _) = value[-1]
        value[-1] = (text, token)
        self.bot_getter().update(value=value)
