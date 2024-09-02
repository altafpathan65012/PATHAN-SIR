#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    pass
    """
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7035220759:AAEQcpQXZOd8aWgJkXQMmUzoeFuU_ufYego")
    API_ID = int(os.environ["API_ID", 23031620]
    API_HASH = os.environ["API_HASH", "31cb00c1cbe580394778b43105864bca"]
    AUTH_USERS = "502980590"""
    WEBHOOK = True  # Don't change this
    PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set

