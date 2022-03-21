#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) Shrimadhav U K
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.


class Translation:
    START_TEXT = (
        "Hello, I'm TGScrapAPID!\n"
        "please read the TnC before proceeding: https://t.me/supbuz\n"
        "Thank you for using me 😬\n"
        "Enter your Telegram Phone Number, "
        "to get the APP-ID from my.telegram.org\n\n"
        "/start at any stage to re-enter your details"
    )
    AFTER_RECVD_CODE_TEXT = (
        "I see!\n"
        "now please send the Telegram code that "
        "you received from Telegram!\n\n"

        "this code is only used for the purpose of "
        "getting the APP ID from my.telegram.org\n"
        "/start and send your detail"
    )
    BEFORE_SUCC_LOGIN = "recieved code. Scarpping web page ..."
    ERRED_PAGE = "something wrong. failed to get app id. \n\n@Kabaridevbot_bot"
    CANCELLED_MESG = "Bye! Please re /start the bot conversation"
    IN_VALID_CODE_PVDED = (
        "sorry, "
        "but the input does not seem to be "
        "a valid Telegram Web-Login code"
    )
    IN_VALID_PHNO_PVDED = (
        "sorry, "
        "but the input does not seem to be "
        "a valid phone number"
    )
