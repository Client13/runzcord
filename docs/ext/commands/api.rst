.. currentmodule:: runzcord

API Reference
===============

The following section outlines the API of runzcord's command extension module.

.. _ext_commands_api_bot:

Bots
------

Bot
~~~~

.. attributetable:: runzcord.ext.commands.Bot

.. autoclass:: runzcord.ext.commands.Bot
    :members:
    :inherited-members:
    :exclude-members: after_invoke, before_invoke, check, check_once, command, event, group, listen, slash_command, user_command, message_command, after_slash_command_invoke, after_user_command_invoke, after_message_command_invoke, before_slash_command_invoke, before_user_command_invoke, before_message_command_invoke

    .. automethod:: Bot.after_invoke()
        :decorator:

    .. automethod:: Bot.after_slash_command_invoke()
        :decorator:

    .. automethod:: Bot.after_user_command_invoke()
        :decorator:

    .. automethod:: Bot.after_message_command_invoke()
        :decorator:

    .. automethod:: Bot.before_invoke()
        :decorator:

    .. automethod:: Bot.before_slash_command_invoke()
        :decorator:

    .. automethod:: Bot.before_user_command_invoke()
        :decorator:

    .. automethod:: Bot.before_message_command_invoke()
        :decorator:

    .. automethod:: Bot.check()
        :decorator:

    .. automethod:: Bot.check_once()
        :decorator:

    .. automethod:: Bot.command(*args, **kwargs)
        :decorator:

    .. automethod:: Bot.slash_command(*args, **kwargs)
        :decorator:

    .. automethod:: Bot.user_command(*args, **kwargs)
        :decorator:

    .. automethod:: Bot.message_command(*args, **kwargs)
        :decorator:

    .. automethod:: Bot.event()
        :decorator:

    .. automethod:: Bot.group(*args, **kwargs)
        :decorator:

    .. automethod:: Bot.listen(name=None)
        :decorator:

AutoShardedBot
~~~~~~~~~~~~~~~~

.. attributetable:: runzcord.ext.commands.AutoShardedBot

.. autoclass:: runzcord.ext.commands.AutoShardedBot
    :members:

InteractionBot
~~~~~~~~~~~~~~~~

.. attributetable:: runzcord.ext.commands.InteractionBot

.. autoclass:: runzcord.ext.commands.InteractionBot
    :members:
    :inherited-members:
    :exclude-members: after_slash_command_invoke, after_user_command_invoke, after_message_command_invoke, before_slash_command_invoke, before_user_command_invoke, before_message_command_invoke, application_command_check, slash_command_check, user_command_check, message_command_check, slash_command_check_once, user_command_check_once, message_command_check_once, event, listen, slash_command, user_command, message_command

    .. automethod:: InteractionBot.after_slash_command_invoke()
        :decorator:

    .. automethod:: InteractionBot.after_user_command_invoke()
        :decorator:

    .. automethod:: InteractionBot.after_message_command_invoke()
        :decorator:

    .. automethod:: InteractionBot.before_slash_command_invoke()
        :decorator:

    .. automethod:: InteractionBot.before_user_command_invoke()
        :decorator:

    .. automethod:: InteractionBot.before_message_command_invoke()
        :decorator:

    .. automethod:: InteractionBot.application_command_check()
        :decorator:

    .. automethod:: InteractionBot.slash_command_check()
        :decorator:

    .. automethod:: InteractionBot.user_command_check()
        :decorator:

    .. automethod:: InteractionBot.message_command_check()
        :decorator:

    .. automethod:: InteractionBot.slash_command_check_once()
        :decorator:

    .. automethod:: InteractionBot.user_command_check_once()
        :decorator:

    .. automethod:: InteractionBot.message_command_check_once()
        :decorator:

    .. automethod:: InteractionBot.slash_command(*args, **kwargs)
        :decorator:

    .. automethod:: InteractionBot.user_command(*args, **kwargs)
        :decorator:

    .. automethod:: InteractionBot.message_command(*args, **kwargs)
        :decorator:

    .. automethod:: InteractionBot.event()
        :decorator:

    .. automethod:: InteractionBot.listen(name=None)
        :decorator:

AutoShardedInteractionBot
~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: runzcord.ext.commands.AutoShardedInteractionBot

.. autoclass:: runzcord.ext.commands.AutoShardedInteractionBot
    :members:

Prefix Helpers
----------------

.. autofunction:: runzcord.ext.commands.when_mentioned

.. autofunction:: runzcord.ext.commands.when_mentioned_or

.. _ext_commands_api_events:

Event Reference
-----------------

These events function similar to :ref:`the regular events <discord-api-events>`, except they
are custom to the command extension module.

.. function:: runzcord.ext.commands.on_command_error(ctx, error)

    An error handler that is called when an error is raised
    inside a command either through user input error, check
    failure, or an error in your own code.

    A default one is provided (:meth:`.Bot.on_command_error`).

    :param ctx: The invocation context.
    :type ctx: :class:`.Context`
    :param error: The error that was raised.
    :type error: :class:`.CommandError` derived

.. function:: runzcord.ext.commands.on_slash_command_error(inter, error)

    An error handler that is called when an error is raised
    inside a slash command either through user input error, check
    failure, or an error in your own code.

    A default one is provided (:meth:`.Bot.on_slash_command_error`).

    :param inter: The interaction that invoked this slash command.
    :type inter: :class:`.ApplicationCommandInteraction`
    :param error: The error that was raised.
    :type error: :class:`.CommandError` derived

.. function:: runzcord.ext.commands.on_user_command_error(inter, error)

    An error handler that is called when an error is raised
    inside a user command either through check
    failure, or an error in your own code.

    A default one is provided (:meth:`.Bot.on_user_command_error`).

    :param inter: The interaction that invoked this user command.
    :type inter: :class:`.ApplicationCommandInteraction`
    :param error: The error that was raised.
    :type error: :class:`.CommandError` derived

.. function:: runzcord.ext.commands.on_message_command_error(inter, error)

    An error handler that is called when an error is raised
    inside a message command either through check
    failure, or an error in your own code.

    A default one is provided (:meth:`.Bot.on_message_command_error`).

    :param inter: The interaction that invoked this message command.
    :type inter: :class:`.ApplicationCommandInteraction`
    :param error: The error that was raised.
    :type error: :class:`.CommandError` derived

.. function:: runzcord.ext.commands.on_command(ctx)

    An event that is called when a command is found and is about to be invoked.

    This event is called regardless of whether the command itself succeeds via
    error or completes.

    :param ctx: The invocation context.
    :type ctx: :class:`.Context`

.. function:: runzcord.ext.commands.on_slash_command(inter)

    An event that is called when a slash command is found and is about to be invoked.

    This event is called regardless of whether the slash command itself succeeds via
    error or completes.

    :param inter: The interaction that invoked this slash command.
    :type inter: :class:`.ApplicationCommandInteraction`

.. function:: runzcord.ext.commands.on_user_command(inter)

    An event that is called when a user command is found and is about to be invoked.

    This event is called regardless of whether the user command itself succeeds via
    error or completes.

    :param inter: The interaction that invoked this user command.
    :type inter: :class:`.ApplicationCommandInteraction`

.. function:: runzcord.ext.commands.on_message_command(inter)

    An event that is called when a message command is found and is about to be invoked.

    This event is called regardless of whether the message command itself succeeds via
    error or completes.

    :param inter: The interaction that invoked this message command.
    :type inter: :class:`.ApplicationCommandInteraction`

.. function:: runzcord.ext.commands.on_command_completion(ctx)

    An event that is called when a command has completed its invocation.

    This event is called only if the command succeeded, i.e. all checks have
    passed and the user input it correctly.

    :param ctx: The invocation context.
    :type ctx: :class:`.Context`

.. function:: runzcord.ext.commands.on_slash_command_completion(inter)

    An event that is called when a slash command has completed its invocation.

    This event is called only if the slash command succeeded, i.e. all checks have
    passed and command handler ran successfully.

    :param inter: The interaction that invoked this slash command.
    :type inter: :class:`.ApplicationCommandInteraction`

.. function:: runzcord.ext.commands.on_user_command_completion(inter)

    An event that is called when a user command has completed its invocation.

    This event is called only if the user command succeeded, i.e. all checks have
    passed and command handler ran successfully.

    :param inter: The interaction that invoked this user command.
    :type inter: :class:`.ApplicationCommandInteraction`

.. function:: runzcord.ext.commands.on_message_command_completion(inter)

    An event that is called when a message command has completed its invocation.

    This event is called only if the message command succeeded, i.e. all checks have
    passed and command handler ran successfully.

    :param inter: The interaction that invoked this message command.
    :type inter: :class:`.ApplicationCommandInteraction`

.. _ext_commands_api_command:

Commands
----------

Decorators
~~~~~~~~~~~~

.. autofunction:: runzcord.ext.commands.command
    :decorator:

.. autofunction:: runzcord.ext.commands.slash_command
    :decorator:

.. autofunction:: runzcord.ext.commands.user_command
    :decorator:

.. autofunction:: runzcord.ext.commands.message_command
    :decorator:

.. autofunction:: runzcord.ext.commands.group
    :decorator:

Helper Functions
~~~~~~~~~~~~~~~~

.. autofunction:: runzcord.ext.commands.Param

.. autofunction:: runzcord.ext.commands.option_enum

.. autofunction:: runzcord.ext.commands.inject

.. autofunction:: runzcord.ext.commands.register_injection
    :decorator:

.. autofunction:: runzcord.ext.commands.converter_method
    :decorator:

Application Command
~~~~~~~~~~~~~~~~~~~

.. attributetable:: runzcord.ext.commands.InvokableApplicationCommand

.. autoclass:: runzcord.ext.commands.InvokableApplicationCommand
    :members:
    :exclude-members: before_invoke, after_invoke, error

    .. automethod:: InvokableApplicationCommand.before_invoke()
        :decorator:

    .. automethod:: InvokableApplicationCommand.after_invoke()
        :decorator:

    .. automethod:: InvokableApplicationCommand.error()
        :decorator:

Slash Command
~~~~~~~~~~~~~

.. attributetable:: runzcord.ext.commands.InvokableSlashCommand

.. autoclass:: runzcord.ext.commands.InvokableSlashCommand
    :members:
    :special-members: __call__
    :exclude-members: sub_command, sub_command_group, after_invoke, before_invoke, error

    .. automethod:: InvokableSlashCommand.sub_command(*args, **kwargs)
        :decorator:

    .. automethod:: InvokableSlashCommand.sub_command_group(*args, **kwargs)
        :decorator:

    .. automethod:: InvokableSlashCommand.after_invoke()
        :decorator:

    .. automethod:: InvokableSlashCommand.before_invoke()
        :decorator:

    .. automethod:: InvokableSlashCommand.error()
        :decorator:

Slash Subcommand
~~~~~~~~~~~~~~~~

.. attributetable:: runzcord.ext.commands.SubCommand

.. autoclass:: runzcord.ext.commands.SubCommand
    :members:
    :exclude-members: after_invoke, before_invoke, error

    .. automethod:: SubCommand.after_invoke()
        :decorator:

    .. automethod:: SubCommand.before_invoke()
        :decorator:

    .. automethod:: SubCommand.error()
        :decorator:

Slash Subcommand Group
~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: runzcord.ext.commands.SubCommandGroup

.. autoclass:: runzcord.ext.commands.SubCommandGroup
    :members:
    :exclude-members: sub_command, after_invoke, before_invoke, error

    .. automethod:: SubCommandGroup.sub_command(*args, **kwargs)
        :decorator:

    .. automethod:: SubCommandGroup.after_invoke()
        :decorator:

    .. automethod:: SubCommandGroup.before_invoke()
        :decorator:

    .. automethod:: SubCommandGroup.error()
        :decorator:

ParamInfo
~~~~~~~~~

.. attributetable:: runzcord.ext.commands.ParamInfo

.. autoclass:: runzcord.ext.commands.ParamInfo

User Command
~~~~~~~~~~~~

.. attributetable:: runzcord.ext.commands.InvokableUserCommand

.. autoclass:: runzcord.ext.commands.InvokableUserCommand
    :members:
    :special-members: __call__
    :exclude-members: after_invoke, before_invoke, error

    .. automethod:: InvokableUserCommand.after_invoke()
        :decorator:

    .. automethod:: InvokableUserCommand.before_invoke()
        :decorator:

    .. automethod:: InvokableUserCommand.error()
        :decorator:

Message Command
~~~~~~~~~~~~~~~

.. attributetable:: runzcord.ext.commands.InvokableMessageCommand

.. autoclass:: runzcord.ext.commands.InvokableMessageCommand
    :members:
    :special-members: __call__
    :exclude-members: after_invoke, before_invoke, error

    .. automethod:: InvokableMessageCommand.after_invoke()
        :decorator:

    .. automethod:: InvokableMessageCommand.before_invoke()
        :decorator:

    .. automethod:: InvokableMessageCommand.error()
        :decorator:

Command
~~~~~~~~~

.. attributetable:: runzcord.ext.commands.Command

.. autoclass:: runzcord.ext.commands.Command
    :members:
    :special-members: __call__
    :exclude-members: after_invoke, before_invoke, error

    .. automethod:: Command.after_invoke()
        :decorator:

    .. automethod:: Command.before_invoke()
        :decorator:

    .. automethod:: Command.error()
        :decorator:

Group
~~~~~~

.. attributetable:: runzcord.ext.commands.Group

.. autoclass:: runzcord.ext.commands.Group
    :members:
    :inherited-members:
    :exclude-members: after_invoke, before_invoke, command, error, group

    .. automethod:: Group.after_invoke()
        :decorator:

    .. automethod:: Group.before_invoke()
        :decorator:

    .. automethod:: Group.command(*args, **kwargs)
        :decorator:

    .. automethod:: Group.error()
        :decorator:

    .. automethod:: Group.group(*args, **kwargs)
        :decorator:

GroupMixin
~~~~~~~~~~~

.. attributetable:: runzcord.ext.commands.GroupMixin

.. autoclass:: runzcord.ext.commands.GroupMixin
    :members:
    :exclude-members: command, group

    .. automethod:: GroupMixin.command(*args, **kwargs)
        :decorator:

    .. automethod:: GroupMixin.group(*args, **kwargs)
        :decorator:

LargeInt
~~~~~~~~

.. autoclass:: runzcord.ext.commands.LargeInt

    This is a class which inherits from :class:`int` to allow large numbers in slash commands, meant to be used only for annotations.

Range
~~~~~

.. autoclass:: runzcord.ext.commands.Range


.. _ext_commands_api_cogs:

Cogs
------

Cog
~~~~

.. attributetable:: runzcord.ext.commands.Cog

.. autoclass:: runzcord.ext.commands.Cog
    :members:

CogMeta
~~~~~~~~

.. attributetable:: runzcord.ext.commands.CogMeta

.. autoclass:: runzcord.ext.commands.CogMeta
    :members:

.. _ext_commands_help_command:

Help Commands
---------------

HelpCommand
~~~~~~~~~~~~

.. attributetable:: runzcord.ext.commands.HelpCommand

.. autoclass:: runzcord.ext.commands.HelpCommand
    :members:

DefaultHelpCommand
~~~~~~~~~~~~~~~~~~~

.. attributetable:: runzcord.ext.commands.DefaultHelpCommand

.. autoclass:: runzcord.ext.commands.DefaultHelpCommand
    :members:
    :exclude-members: send_bot_help, send_cog_help, send_group_help, send_command_help, prepare_help_command

MinimalHelpCommand
~~~~~~~~~~~~~~~~~~~

.. attributetable:: runzcord.ext.commands.MinimalHelpCommand

.. autoclass:: runzcord.ext.commands.MinimalHelpCommand
    :members:
    :exclude-members: send_bot_help, send_cog_help, send_group_help, send_command_help, prepare_help_command

Paginator
~~~~~~~~~~

.. attributetable:: runzcord.ext.commands.Paginator

.. autoclass:: runzcord.ext.commands.Paginator
    :members:

Enums
------

.. class:: BucketType
    :module: runzcord.ext.commands

    Specifies a type of bucket for, e.g. a cooldown.

    .. attribute:: default

        The default bucket operates on a global basis.
    .. attribute:: user

        The user bucket operates on a per-user basis.
    .. attribute:: guild

        The guild bucket operates on a per-guild basis.
    .. attribute:: channel

        The channel bucket operates on a per-channel basis.
    .. attribute:: member

        The member bucket operates on a per-member basis.
    .. attribute:: category

        The category bucket operates on a per-category basis.
    .. attribute:: role

        The role bucket operates on a per-role basis.

        .. versionadded:: 1.3


.. _ext_commands_api_checks:

Checks
-------

.. autofunction:: runzcord.ext.commands.check(predicate)
    :decorator:

.. autofunction:: runzcord.ext.commands.check_any(*checks)
    :decorator:

.. autofunction:: runzcord.ext.commands.has_role(item)
    :decorator:

.. autofunction:: runzcord.ext.commands.has_permissions(**perms)
    :decorator:

.. autofunction:: runzcord.ext.commands.has_guild_permissions(**perms)
    :decorator:

.. autofunction:: runzcord.ext.commands.has_any_role(*items)
    :decorator:

.. autofunction:: runzcord.ext.commands.bot_has_role(item)
    :decorator:

.. autofunction:: runzcord.ext.commands.bot_has_permissions(**perms)
    :decorator:

.. autofunction:: runzcord.ext.commands.bot_has_guild_permissions(**perms)
    :decorator:

.. autofunction:: runzcord.ext.commands.bot_has_any_role(*items)
    :decorator:

.. autofunction:: runzcord.ext.commands.cooldown(rate, per, type=runzcord.ext.commands.BucketType.default)
    :decorator:

.. autofunction:: runzcord.ext.commands.dynamic_cooldown(cooldown, type=BucketType.default)
    :decorator:

.. autofunction:: runzcord.ext.commands.max_concurrency(number, per=runzcord.ext.commands.BucketType.default, *, wait=False)
    :decorator:

.. autofunction:: runzcord.ext.commands.before_invoke(coro)
    :decorator:

.. autofunction:: runzcord.ext.commands.after_invoke(coro)
    :decorator:

.. autofunction:: runzcord.ext.commands.guild_only(,)
    :decorator:

.. autofunction:: runzcord.ext.commands.dm_only(,)
    :decorator:

.. autofunction:: runzcord.ext.commands.is_owner(,)
    :decorator:

.. autofunction:: runzcord.ext.commands.is_nsfw(,)
    :decorator:

.. autofunction:: runzcord.ext.commands.default_member_permissions
    :decorator:

.. _ext_commands_api_context:

Cooldown
---------

.. attributetable:: runzcord.ext.commands.Cooldown

.. autoclass:: runzcord.ext.commands.Cooldown
    :members:

Context
--------

.. attributetable:: runzcord.ext.commands.Context

.. autoclass:: runzcord.ext.commands.Context
    :members:
    :inherited-members:
    :exclude-members: history, typing

    .. automethod:: runzcord.ext.commands.Context.history
        :async-for:

    .. automethod:: runzcord.ext.commands.Context.typing
        :async-with:

.. _ext_commands_api_converters:

Converters
------------

.. autoclass:: runzcord.ext.commands.Converter
    :members:

.. autoclass:: runzcord.ext.commands.ObjectConverter
    :members:

.. autoclass:: runzcord.ext.commands.MemberConverter
    :members:

.. autoclass:: runzcord.ext.commands.UserConverter
    :members:

.. autoclass:: runzcord.ext.commands.MessageConverter
    :members:

.. autoclass:: runzcord.ext.commands.PartialMessageConverter
    :members:

.. autoclass:: runzcord.ext.commands.GuildChannelConverter
    :members:

.. autoclass:: runzcord.ext.commands.TextChannelConverter
    :members:

.. autoclass:: runzcord.ext.commands.VoiceChannelConverter
    :members:

.. autoclass:: runzcord.ext.commands.StageChannelConverter
    :members:

.. autoclass:: runzcord.ext.commands.CategoryChannelConverter
    :members:

.. autoclass:: runzcord.ext.commands.ForumChannelConverter
    :members:

.. autoclass:: runzcord.ext.commands.ThreadConverter
    :members:

.. autoclass:: runzcord.ext.commands.ColourConverter
    :members:

.. autoclass:: runzcord.ext.commands.RoleConverter
    :members:

.. autoclass:: runzcord.ext.commands.GameConverter
    :members:

.. autoclass:: runzcord.ext.commands.InviteConverter
    :members:

.. autoclass:: runzcord.ext.commands.GuildConverter
    :members:

.. autoclass:: runzcord.ext.commands.EmojiConverter
    :members:

.. autoclass:: runzcord.ext.commands.PartialEmojiConverter
    :members:

.. autoclass:: runzcord.ext.commands.GuildStickerConverter
    :members:

.. autoclass:: runzcord.ext.commands.PermissionsConverter
    :members:

.. autoclass:: runzcord.ext.commands.GuildScheduledEventConverter
    :members:

.. autoclass:: runzcord.ext.commands.clean_content
    :members:

.. autoclass:: runzcord.ext.commands.Greedy()

.. autofunction:: runzcord.ext.commands.run_converters

Flag Converter
~~~~~~~~~~~~~~~

.. autoclass:: runzcord.ext.commands.FlagConverter
    :members:

.. autoclass:: runzcord.ext.commands.Flag()
    :members:

.. autofunction:: runzcord.ext.commands.flag

.. _ext_commands_api_errors:

Exceptions
-----------

.. autoexception:: runzcord.ext.commands.CommandError
    :members:

.. autoexception:: runzcord.ext.commands.ConversionError
    :members:

.. autoexception:: runzcord.ext.commands.MissingRequiredArgument
    :members:

.. autoexception:: runzcord.ext.commands.ArgumentParsingError
    :members:

.. autoexception:: runzcord.ext.commands.UnexpectedQuoteError
    :members:

.. autoexception:: runzcord.ext.commands.InvalidEndOfQuotedStringError
    :members:

.. autoexception:: runzcord.ext.commands.ExpectedClosingQuoteError
    :members:

.. autoexception:: runzcord.ext.commands.BadArgument
    :members:

.. autoexception:: runzcord.ext.commands.BadUnionArgument
    :members:

.. autoexception:: runzcord.ext.commands.BadLiteralArgument
    :members:

.. autoexception:: runzcord.ext.commands.PrivateMessageOnly
    :members:

.. autoexception:: runzcord.ext.commands.NoPrivateMessage
    :members:

.. autoexception:: runzcord.ext.commands.CheckFailure
    :members:

.. autoexception:: runzcord.ext.commands.CheckAnyFailure
    :members:

.. autoexception:: runzcord.ext.commands.CommandNotFound
    :members:

.. autoexception:: runzcord.ext.commands.DisabledCommand
    :members:

.. autoexception:: runzcord.ext.commands.CommandInvokeError
    :members:

.. autoexception:: runzcord.ext.commands.TooManyArguments
    :members:

.. autoexception:: runzcord.ext.commands.UserInputError
    :members:

.. autoexception:: runzcord.ext.commands.CommandOnCooldown
    :members:

.. autoexception:: runzcord.ext.commands.MaxConcurrencyReached
    :members:

.. autoexception:: runzcord.ext.commands.NotOwner
    :members:

.. autoexception:: runzcord.ext.commands.ObjectNotFound
    :members:

.. autoexception:: runzcord.ext.commands.MessageNotFound
    :members:

.. autoexception:: runzcord.ext.commands.MemberNotFound
    :members:

.. autoexception:: runzcord.ext.commands.GuildNotFound
    :members:

.. autoexception:: runzcord.ext.commands.UserNotFound
    :members:

.. autoexception:: runzcord.ext.commands.ChannelNotFound
    :members:

.. autoexception:: runzcord.ext.commands.ChannelNotReadable
    :members:

.. autoexception:: runzcord.ext.commands.ThreadNotFound
    :members:

.. autoexception:: runzcord.ext.commands.BadColourArgument
    :members:

.. autoexception:: runzcord.ext.commands.RoleNotFound
    :members:

.. autoexception:: runzcord.ext.commands.BadInviteArgument
    :members:

.. autoexception:: runzcord.ext.commands.EmojiNotFound
    :members:

.. autoexception:: runzcord.ext.commands.PartialEmojiConversionFailure
    :members:

.. autoexception:: runzcord.ext.commands.GuildStickerNotFound
    :members:

.. autoexception:: runzcord.ext.commands.GuildScheduledEventNotFound
    :members:

.. autoexception:: runzcord.ext.commands.BadBoolArgument
    :members:

.. autoexception:: runzcord.ext.commands.LargeIntConversionFailure
    :members:

.. autoexception:: runzcord.ext.commands.MissingPermissions
    :members:

.. autoexception:: runzcord.ext.commands.BotMissingPermissions
    :members:

.. autoexception:: runzcord.ext.commands.MissingRole
    :members:

.. autoexception:: runzcord.ext.commands.BotMissingRole
    :members:

.. autoexception:: runzcord.ext.commands.MissingAnyRole
    :members:

.. autoexception:: runzcord.ext.commands.BotMissingAnyRole
    :members:

.. autoexception:: runzcord.ext.commands.NSFWChannelRequired
    :members:

.. autoexception:: runzcord.ext.commands.FlagError
    :members:

.. autoexception:: runzcord.ext.commands.BadFlagArgument
    :members:

.. autoexception:: runzcord.ext.commands.MissingFlagArgument
    :members:

.. autoexception:: runzcord.ext.commands.TooManyFlags
    :members:

.. autoexception:: runzcord.ext.commands.MissingRequiredFlag
    :members:

.. autoexception:: runzcord.ext.commands.ExtensionError
    :members:

.. autoexception:: runzcord.ext.commands.ExtensionAlreadyLoaded
    :members:

.. autoexception:: runzcord.ext.commands.ExtensionNotLoaded
    :members:

.. autoexception:: runzcord.ext.commands.NoEntryPointError
    :members:

.. autoexception:: runzcord.ext.commands.ExtensionFailed
    :members:

.. autoexception:: runzcord.ext.commands.ExtensionNotFound
    :members:

.. autoexception:: runzcord.ext.commands.CommandRegistrationError
    :members:


Exception Hierarchy
~~~~~~~~~~~~~~~~~~~~~

.. exception_hierarchy::

    - :exc:`~.DiscordException`
        - :exc:`~.commands.CommandError`
            - :exc:`~.commands.ConversionError`
            - :exc:`~.commands.UserInputError`
                - :exc:`~.commands.MissingRequiredArgument`
                - :exc:`~.commands.TooManyArguments`
                - :exc:`~.commands.BadArgument`
                    - :exc:`~.commands.ObjectNotFound`
                    - :exc:`~.commands.MemberNotFound`
                    - :exc:`~.commands.GuildNotFound`
                    - :exc:`~.commands.UserNotFound`
                    - :exc:`~.commands.MessageNotFound`
                    - :exc:`~.commands.ChannelNotReadable`
                    - :exc:`~.commands.ChannelNotFound`
                    - :exc:`~.commands.ThreadNotFound`
                    - :exc:`~.commands.BadColourArgument`
                    - :exc:`~.commands.RoleNotFound`
                    - :exc:`~.commands.BadInviteArgument`
                    - :exc:`~.commands.EmojiNotFound`
                    - :exc:`~.commands.PartialEmojiConversionFailure`
                    - :exc:`~.commands.GuildStickerNotFound`
                    - :exc:`~.commands.GuildScheduledEventNotFound`
                    - :exc:`~.commands.BadBoolArgument`
                    - :exc:`~.commands.LargeIntConversionFailure`
                    - :exc:`~.commands.FlagError`
                        - :exc:`~.commands.BadFlagArgument`
                        - :exc:`~.commands.MissingFlagArgument`
                        - :exc:`~.commands.TooManyFlags`
                        - :exc:`~.commands.MissingRequiredFlag`
                - :exc:`~.commands.BadUnionArgument`
                - :exc:`~.commands.BadLiteralArgument`
                - :exc:`~.commands.ArgumentParsingError`
                    - :exc:`~.commands.UnexpectedQuoteError`
                    - :exc:`~.commands.InvalidEndOfQuotedStringError`
                    - :exc:`~.commands.ExpectedClosingQuoteError`
            - :exc:`~.commands.CommandNotFound`
            - :exc:`~.commands.CheckFailure`
                - :exc:`~.commands.CheckAnyFailure`
                - :exc:`~.commands.PrivateMessageOnly`
                - :exc:`~.commands.NoPrivateMessage`
                - :exc:`~.commands.NotOwner`
                - :exc:`~.commands.MissingPermissions`
                - :exc:`~.commands.BotMissingPermissions`
                - :exc:`~.commands.MissingRole`
                - :exc:`~.commands.BotMissingRole`
                - :exc:`~.commands.MissingAnyRole`
                - :exc:`~.commands.BotMissingAnyRole`
                - :exc:`~.commands.NSFWChannelRequired`
            - :exc:`~.commands.DisabledCommand`
            - :exc:`~.commands.CommandInvokeError`
            - :exc:`~.commands.CommandOnCooldown`
            - :exc:`~.commands.MaxConcurrencyReached`
        - :exc:`~.commands.ExtensionError`
            - :exc:`~.commands.ExtensionAlreadyLoaded`
            - :exc:`~.commands.ExtensionNotLoaded`
            - :exc:`~.commands.NoEntryPointError`
            - :exc:`~.commands.ExtensionFailed`
            - :exc:`~.commands.ExtensionNotFound`
    - :exc:`~.ClientException`
        - :exc:`~.commands.CommandRegistrationError`

Warnings
----------

.. autoclass:: runzcord.ext.commands.MessageContentPrefixWarning

Warning Hierarchy
~~~~~~~~~~~~~~~~~~~

.. exception_hierarchy::

    - :class:`DiscordWarning`
        - :class:`~.commands.MessageContentPrefixWarning`
