from agents import call_llm, extract_json
from collections import Counter

SYS = "You are a logical AI. ALWAYS output valid JSON: {\"reasoning\": \"string\", \"move\": int_or_list}. No other text."


def run_single_agent(rules, state):
    out = extract_json(call_llm(SYS, f"Rules: {rules}\nState: {state}"))
    return out if out else {"move": None}, ["Single Call"]


def run_parallel_agent(rules, state):
    moves = []
    for _ in range(3):
        data = extract_json(call_llm(SYS, f"Rules: {rules}\nState: {state}"))
        if data and "move" in data:
            moves.append(tuple(data['move']) if isinstance(
                data['move'], list) else data['move'])
    if not moves:
        return {"move": None}, ["All Failed"]
    best = Counter(moves).most_common(1)[0][0]
    return {"move": list(best) if isinstance(best, tuple) else best}, [f"Votes: {moves}"]


def run_hierarchical_agent(rules, state):
    r_out = extract_json(call_llm(SYS + " (Reasoner)",
                         f"Rules: {rules}\nState: {state}\nOutput JSON."))
    c_out = extract_json(call_llm(
        SYS + " (Critic)", f"Critique this move: {r_out} for state: {state}\nOutput JSON."))
    f_out = extract_json(call_llm(
        SYS + " (Manager)", f"Based on Reasoner {r_out} and Critic {c_out}, make final move.\nOutput JSON."))
    return f_out if f_out else {"move": None}, [str(r_out), str(c_out), str(f_out)]
