"""This module contains decorator that checks function behaviour."""
from functools import wraps


class ContractError(Exception):
    """We use this error when someone breaks our contract."""


#: Special value, that indicates that validation for this type is not required.
Any = object()


def contract(arg_types=None, return_type=None, raises=None):
    """
    Decorator for checking function behaviour.

    Parameters:
        arg_types: Types of function arguments
        return_type: Type of function returned value
        raises: Exceptions that function can throw

    Returns:
        function_return: Return of a decorated function

    Raises:
        ContractError: if function raises an error that is not in errors
        raises: Exception that function can raise
    """
    def factory(function):
        @wraps(function)
        def decorator(*args):
            if arg_types is not None:
                for (arg_type, arg) in zip(arg_types, args):
                    if arg_type is not Any and not isinstance(arg, arg_type):
                        raise ContractError('Wrong argument type')

            if raises is None:
                f_r = function(*args)
            else:
                try:
                    f_r = function(*args)
                except raises:
                    raise
                except Exception as exc:
                    raise ContractError('Exception not from raises') from exc

            if return_type is not None and not isinstance(f_r, return_type):
                raise ContractError('Wrong return type')

            return f_r
        return decorator
    return factory
