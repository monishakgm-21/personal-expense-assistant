# Personal Expense Assistant - Analysis

## 1. Scenario

The chosen private-data scenario is a Personal Expense Assistant. The system works with personal expense records such as date, category, description, and amount. The same expense data is used to demonstrate three different approaches: Plain Chatbot, Rule-Based Workflow, and AI Agent.

## 2. Plain Chatbot

The Plain Chatbot provides a simple conversational interface for the user. It reads the private expense data and answers basic questions based on predefined conditions. For example, it can calculate the total amount spent on food or shopping.

The main advantage is simplicity. It is easy to build and understand. However, its flexibility is limited because new types of questions require additional conditions to be added manually. It does not independently decide which tools or actions are required.

## 3. Rule-Based Workflow

The Rule-Based Workflow directly processes the private expense data using predefined programming rules. It calculates the total spending, category-wise spending, and identifies spending levels using fixed conditions.

This approach is predictable and reliable for clearly defined tasks. However, the workflow follows fixed rules and cannot easily adapt to unexpected user requests. Any new decision or behaviour generally requires changes to the program logic.

## 4. AI Agent

The AI Agent uses multiple tools to work with the private expense data. The agent can select the appropriate operation based on the user's request. The tools include reading expense data, calculating category totals, calculating overall spending, and finding the highest spending category.

The agent can also handle a multi-step request such as finding the total spending and the category with the highest spending. This makes the approach more flexible for tasks that require multiple operations.

## 5. Comparison

| Criteria | Plain Chatbot | Rule-Based Workflow | AI Agent |
|---|---|---|---|
| Flexibility | Limited | Low | Higher |
| Decision-making | Basic predefined conditions | Fixed rules | Can select suitable tools |
| Tool usage | Limited | Program functions | Multiple tools |
| Private-data access | Yes | Yes | Yes |
| Multi-step task handling | Limited | Predefined steps | Supports multiple operations |
| Automation | Basic | High for fixed tasks | Higher for flexible tasks |
| Reliability | High for simple supported questions | High and predictable | Depends on agent logic and tools |

## 6. Suitability

The Plain Chatbot is suitable for simple questions where the expected inputs and outputs are known in advance.

The Rule-Based Workflow is suitable when the process is fixed and predictable. It is useful when consistent and repeatable results are important.

The AI Agent is suitable when the user may ask different types of questions and the system needs to select different tools or perform multiple operations.

## 7. Conclusion

All three approaches can work with the same private expense data, but they solve the problem differently. The Plain Chatbot focuses on simple interaction, the Rule-Based Workflow focuses on fixed and predictable processing, and the AI Agent focuses on flexible tool-based task handling.

The experiment demonstrates how the same private-data problem can be implemented using different levels of automation and decision-making.