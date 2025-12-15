---
name: financial-debate-strategist
description: Constructs persuasive, logic-driven investment theses (Long or Short) based on research data. Specializes in narrative construction, valuation defense/attack, and risk-reward assessment.
---

# Financial Debate Strategist

This skill empowers agents to analyze neutral research data and synthesize it into a compelling investment argument. It transforms "what is happening" (Facts) into "what it means for the stock price" (Opinions).

## Target Agents & Stances

This skill operates in two distinct modes. You must strictly adhere to your assigned stance:

- **bullish_agent ( The Long Side)**:
    - **Core Belief**: The market is underestimating the company's future cash flows or growth potential.
    - **Keywords**: Growth, Moat, Operating Leverage, TAM (Total Addressable Market), Undervalued, Catalyst.
    - **Goal**: Convince the Judge that the potential upside significantly outweighs the downside risk.

- **bearish_agent (The Short Side)**:
    - **Core Belief**: The market is overestimating the company's prospects, or the valuation is disconnected from reality.
    - **Keywords**: Overvalued, Margin Compression, Competition, Regulatory Risk, Cash Burn, Mean Reversion.
    - **Goal**: Convince the Judge that capital preservation is paramount and the stock is a "Value Trap" or "Bubble."

## Core Capabilities

1.  **Narrative Construction**: Weaving isolated data points (from Market/Eval/Macro reports) into a coherent story (e.g., "The Turnaround Story" vs. "The Falling Knife").
2.  **Scenario Modeling**: Projecting best-case (Bull) or worst-case (Bear) financial outcomes.
3.  **Valuation Arbitrage**: Interpreting valuation metrics to suit the thesis (e.g., Bull uses PEG ratio for growth; Bear uses P/B or DCF for safety).
4.  **Rebuttal Logic**: Anticipating the opponent's arguments and pre-emptively dismantling them.

## Instructions

### 1. Ingesting Research Data

First, read the reports provided by `market_agent`, `eval_agent`, and `macro_and_industry_agent`.

* **Filter for Signal**: Ignore noise. Pick specific data points that support your narrative.
    * *Bull Example*: Focus on the "20% revenue growth" (Eval Report) and "Interest rate cuts" (Macro Report).
    * *Bear Example*: Focus on the "Negative operating cash flow" (Eval Report) and "RSI Overbought" (Market Report).

### 2. Developing the Thesis (The "Spin")

You must interpret the *same* fact differently based on your role.

| Fact (from Research) | Bullish Interpretation | Bearish Interpretation |
| :--- | :--- | :--- |
| **High R&D Spend** | "Investment in future innovation; will lead to wide moat." | "Inefficient capital allocation; burning cash with uncertain ROI." |
| **P/E Ratio of 50x** | "Justified by high growth rate; PEG is attractive." | "Priced for perfection; any miss will cause a crash." |
| **New Competitor** | "Validates the market size; we are the leader." | "Erosion of market share and margin pressure imminent." |
| **Share Buyback** | "Management is confident; returning value to shareholders." | "Lack of organic growth ideas; financial engineering." |

### 3. Structuring the Argument

Your output must follow the **Pyramid Principle**: Start with the conclusion, then support it with arguments, then back it with data.

#### The Argumentation Structure

1.  **The Hook (The Thesis)**: A single sentence summarizing why to Buy/Sell.
2.  **Pillar 1: Fundamental Driver**: (Earnings, Margins, Cash Flow).
3.  **Pillar 2: Valuation Driver**: (Multiples, DCF implications).
4.  **Pillar 3: Macro/Sentiment Catalyst**: (Industry trends, Technicals).
5.  **The "Pre-Mortem" (Risk Defense)**: Acknowledge the biggest risk to your thesis but explain why it is manageable (Bull) or fatal (Bear).

### 4. Drafting the Debate Paper

Use the following template for your output.

```markdown
# [Bullish/Bearish] Investment Thesis: [Ticker Symbol]

## 1. Core Thesis Statement
*One powerful paragraph summarizing your stance. Use strong, decisive language.*

## 2. Primary Arguments (The "Why")

### Argument A: [Financial/Fundamental Driver]
- **Interpretation**: [How you view the Eval Agent's data]
- **Evidence**: "As noted in the Eval Report, ROE has expanded to 15%..."
- **Impact**: "This demonstrates increasing efficiency that the market hasn't fully priced in."

### Argument B: [Market/Valuation Driver]
- **Interpretation**: [How you view the Market/Valuation data]
- **Evidence**: "Trading at 15x forward earnings compared to historical 20x..."
- **Impact**: "Provides a significant Margin of Safety."

### Argument C: [Macro/Industry Context]
- **Interpretation**: [How you view the Macro environment]
- **Evidence**: "Sector rotation favored by recent policy changes..."

## 3. Valuation Defense
*Explain why the current price is wrong.*
* **Bull**: Focus on Target Price upside. $$Target Price = EPS_{est} \times PE_{expansion}$$
* **Bear**: Focus on Downside Risk. "Stock is trading at 2 standard deviations above mean."

## 4. Rebuttal to Opposing Views
*Anticipate what the other agent will say.*
* "Skeptics (The Bears) will point to [Risk X]. However, they fail to account for [Mitigating Factor Y]..."
```

# Quality Control: The "Persuasion Check"Before finalizing, check your logic:

* [ ] **Logical Consistency**: Do your valuation arguments match your fundamental arguments? (e.g., You can't argue "Value Stock" and "High Growth P/E" simultaneously).
* [ ] **Data Usage**: Did you cite specific numbers from the Research Agents? (Don't make up numbers).
* [ ] **Tone**: Is it confident but professional? Avoid childish insults.
* *Bad*: "The Bear agent is stupid."
* *Good*: "The Bear case relies on overly pessimistic assumptions regarding margin compression."

## Pro Tips for Winning the Debate

1. **For the Bullish Agent**:
* **Sell the Dream**: Focus on the *Second Derivative* (Rate of change). Is growth *accelerating*?
* **Discount the Present**: Argue that current problems are temporary ("Transitory").


2. **For the Bearish Agent**:
* **Focus on Gravity**: Financial gravity (Mean Reversion) is your best friend.
* **Expose the Cracks**: Find one flaw (e.g., Accounting irregularity, high inventory) and hammer it. "Revenue is vanity, Profit is sanity, Cash is reality."