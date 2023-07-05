import os
from enum import Enum

from pydantic import BaseSettings, root_validator


class EnvConfig(BaseSettings):
    """Our default configuration for models that should load from .env files."""

    class Config:
        """Specify what .env files to load, and how to load them."""

        env_file = ".env.server", ".env",
        env_file_encoding = "utf-8"
        env_nested_delimiter = "__"


class _Miscellaneous(EnvConfig):
    debug = True
    file_logs = False


Miscellaneous = _Miscellaneous()

FILE_LOGS = Miscellaneous.file_logs
DEBUG_MODE = Miscellaneous.debug


class _Bot(EnvConfig):
    EnvConfig.Config.env_prefix = "bot_"

    prefix = "!"
    sentry_dsn = ""
    token = ""
    trace_loggers = "*"


Bot = _Bot()

class _Colours(EnvConfig):
    EnvConfig.Config.env_prefix = "colours_"

    blue = 0x3775a8
    bright_green = 0x01d277
    orange = 0xe67e22
    pink = 0xcf84e0
    purple = 0xb734eb
    soft_green = 0x68c290
    soft_orange = 0xf9cb54
    soft_red = 0xcd6d6d
    white = 0xfffffe
    yellow = 0xffd241

    @root_validator(pre=True)
    def parse_hex_values(cls, values: dict) -> dict:  # noqa: N805
        """Convert hex strings to ints."""
        for key, value in values.items():
            values[key] = int(value, 16)
        return values


Colours = _Colours()


class _Icons(EnvConfig):
    EnvConfig.Config.env_prefix = "icons_"

    crown_blurple = "https://cdn.discordapp.com/emojis/469964153289965568.png"
    crown_green = "https://cdn.discordapp.com/emojis/469964154719961088.png"
    crown_red = "https://cdn.discordapp.com/emojis/469964154879344640.png"

    defcon_denied = "https://cdn.discordapp.com/emojis/472475292078964738.png"
    defcon_shutdown = "https://cdn.discordapp.com/emojis/470326273952972810.png"
    defcon_unshutdown = "https://cdn.discordapp.com/emojis/470326274213150730.png"
    defcon_update = "https://cdn.discordapp.com/emojis/472472638342561793.png"

    filtering = "https://cdn.discordapp.com/emojis/472472638594482195.png"

    green_checkmark = "https://raw.githubusercontent.com/python-discord/branding/main/icons/checkmark/green-checkmark-dist.png"
    green_questionmark = "https://raw.githubusercontent.com/python-discord/branding/main/icons/checkmark/green-question-mark-dist.png"
    guild_update = "https://cdn.discordapp.com/emojis/469954765141442561.png"

    hash_blurple = "https://cdn.discordapp.com/emojis/469950142942806017.png"
    hash_green = "https://cdn.discordapp.com/emojis/469950144918585344.png"
    hash_red = "https://cdn.discordapp.com/emojis/469950145413251072.png"

    message_bulk_delete = "https://cdn.discordapp.com/emojis/469952898994929668.png"
    message_delete = "https://cdn.discordapp.com/emojis/472472641320648704.png"
    message_edit = "https://cdn.discordapp.com/emojis/472472638976163870.png"

    pencil = "https://cdn.discordapp.com/emojis/470326272401211415.png"

    questionmark = "https://cdn.discordapp.com/emojis/512367613339369475.png"

    remind_blurple = "https://cdn.discordapp.com/emojis/477907609215827968.png"
    remind_green = "https://cdn.discordapp.com/emojis/477907607785570310.png"
    remind_red = "https://cdn.discordapp.com/emojis/477907608057937930.png"

    sign_in = "https://cdn.discordapp.com/emojis/469952898181234698.png"
    sign_out = "https://cdn.discordapp.com/emojis/469952898089091082.png"

    superstarify = "https://cdn.discordapp.com/emojis/636288153044516874.png"
    unsuperstarify = "https://cdn.discordapp.com/emojis/636288201258172446.png"

    token_removed = "https://cdn.discordapp.com/emojis/470326273298792469.png"  # noqa: S105

    user_ban = "https://cdn.discordapp.com/emojis/469952898026045441.png"
    user_timeout = "https://cdn.discordapp.com/emojis/472472640100106250.png"
    user_unban = "https://cdn.discordapp.com/emojis/469952898692808704.png"
    user_untimeout = "https://cdn.discordapp.com/emojis/472472639206719508.png"
    user_update = "https://cdn.discordapp.com/emojis/469952898684551168.png"
    user_verified = "https://cdn.discordapp.com/emojis/470326274519334936.png"
    user_warn = "https://cdn.discordapp.com/emojis/470326274238447633.png"

    voice_state_blue = "https://cdn.discordapp.com/emojis/656899769662439456.png"
    voice_state_green = "https://cdn.discordapp.com/emojis/656899770094452754.png"
    voice_state_red = "https://cdn.discordapp.com/emojis/656899769905709076.png"


Icons = _Icons()


# Bot replies
NEGATIVE_REPLIES = [
    "Noooooon !!",
    "Non.",
    "Je suis désolé Dave, j'ai peur de ne pas pouvoir faire ça.",
    "Je ne pense pas.",
    "Ça n'arrivera pas.",
    "Hors de question.",
    "Hein ? Non.",
    "Nan.",
    "Non.",
    "Peu probable.",
    "Pas question, José.",
    "Pas dans un million d'années.",
    "Aucune chance.",
    "Certainement pas.",
    "NÉGATIF.",
    "Non-non.",
    "Pas chez moi !",
]

POSITIVE_REPLIES = [
    "Oui.",
    "Absolument !",
    "Je peux le faire !",
    "Affirmatif !",
    "Ouais, d'accord.",
    "Bien sûr.",
    "Pas de problème !",
    "Tu es le patron !",
    "D'accord.",
    "Aucun problème.",
    "Je m'en occupe.",
    "D'accord.",
    "C'est comme si c'était fait !",
    "BIEN REÇU",
    "Bien sûr !",
    "A vos ordres, Capitaine !",
    "Je l'accepte.",
]

ERROR_REPLIES = [
    "S'il te plaît, ne fais pas ça.",
    "Tu dois arrêter.",
    "Ça te dérange ?",
    "À l'avenir, ne fais pas ça.",
    "C'était une erreur.",
    "Tu as tout gâché.",
    "Tu es nul en informatique.",
    "Essaies-tu de me tuer ?",
    "Noooooon !!",
    "Je n'arrive pas à croire que tu aies fait ça",
]
