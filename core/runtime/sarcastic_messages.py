import random

MESSAGES = {
    "too_many_vars": [
        "Whoa there, five variables? What is this, NASA?",
        "You really thought I'd let you manage more than 5 variables?",
        "Ever heard of minimalism? Apparently not.",
    ],
    "redeclare_var": [
        "Trying to reinvent the same variable? Bold move...",
        "Yeah, that name was *so* original the first time.",
    ],
    "undefined_var": [
        "Using undefined variables - are you okay?",
        "You're making things up again, aren't you?",
    ],
    "emoji_missing": [
        "You forgot the emoji. This language requires 'vibes'",
        "No emoji? No execution. Rules are rules",
        "You're missing an emoji, you emotionless robot.",
    ],
    "missing_comment": [
        "Where's your comment? Explain yousrelf",
        "No comment? I see you're trying to be mysterious",
        "You forgot the mandatory commentary. Shame.",
    ],
    "unknown_token": [
        "What even is that? I don't speak gibberish",
        "I refuse to acknowledge that token's existence",
    ],
    "expected_value": [
        "Expected something else, but sure, give me this nonsense",
        "Do you even read your own syntax?",
    ],
    "expected_token": [
        "That's not what I asked for. Try again",
        "You had job: give me the right token",
    ],
    "unexpected_token": [
        "This token is as unexpected as your behavior",
        "That's not even close to valid. Try harder",
    ],
    "unexpected_eof": [
        "You ran out of code. Again",
        "The end came sooner than expected",
    ],
    "zero_division": [
        "Nice try. Divide by zero and break the world why don't you",
        "Math called. It says 'no' to dividing by zero",
    ],
    "bad_math": [
        "Math broke. So did my faith in your logic",
    ],
    "arg_count_mismatch": [
        "Function call mismatch. You're either forgetting friends or bringing extras",
        "Wrong number of arguments - this isn't open mic night.",
    ],
    "redeclare_func": [
        "Functoin already exists. Get your own name.",
        "That function was declared already. Copycat",
    ],
    "undefined_func": [
        "Calling a function that doesn't exist? Bold..",
    ],
    "unsupported_ast": [
        "That syntax isn't supported. Nor is your attitude"
    ],
    "unsupported": [
        "Yeah... I'm not doing that yet",
        "Functionality coming soon. Maybe. Probably not"
    ]
}

def get_sarcastic_message(error_type: str) -> str:
    return random.choice(MESSAGES.get(error_type, ["Something went wrong. And it's your fault"]))