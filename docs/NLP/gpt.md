# GPT

## utilize tool in GPT

LLM 是问答对话。

想要在 LLM 里使用工具，譬如说 google search.

> 在聊天机器人 chatdoc 使用 Recommendation tool。

### Call Function

Process:

1. Define tools
    1. Name
    2. Description：When to call
    3. Parameters
    4. （application API？）
2. REACT prompt
    使用 `str{}.format()` 格式

> ```python
> Thought
> Action {Search}
> Input {query}
> Observation {}
> Final Answer {}
> ```

!!! danger "会不会出现 infinite loop 致使 quota | local memory 被消耗完"
