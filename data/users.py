from dataclasses import dataclass

@dataclass(frozen=True)
class User:
    username: str
    password: str
    description: str

PASSWORD = "secret_sauce"

STANDARD_USER = User(
    username="standard_user",
    password=PASSWORD,
    description="Default user",
)

LOCKED_USER = User(
    username="locked_out_user",
    password=PASSWORD,
    description="Blocked user",
)

PROBLEM_USER = User(
    username="problem_user",
    password=PASSWORD,
    description="Broken images, incorrect sorting",
)

PERFORMANCE_USER = User(
    username="performance_glitch_user",
    password=PASSWORD,
    description="Problems with performance",
)

ERROR_USER = User(
    username="error_user",
    password=PASSWORD,
    description="Errors on bucket interaction",
)

VISUAL_USER = User(
    username="visual_user",
    password=PASSWORD,
    description="Visual problems user",
)