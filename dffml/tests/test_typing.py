from typing import Dict, Any, NamedTuple, Optional
from typing import NewType
from dataclasses import dataclass

# from dffml.df.types import Definition


class Definition:
    """
    List[type] is how to specify a list
    """

    def __new__(cls, *args, **kwargs):
        obj = super().__new__(cls)
        # print(f"New was called,{args}\n kwargs : {kwargs}")
        obj.__init__(*args, **kwargs)
        custom_obj = NewType(obj.name, obj.primitive)
        # custom_obj = type(obj.name,)
        # custom_obj.name = obj.name
        # custom_obj.lock = obj.lock
        # custom_obj.spec = obj.spec
        print("yes")
        return custom_obj

    def __init__(
        self,
        name: str,
        primitive: str,
        lock: bool = False,
        spec: Optional[NamedTuple] = None,
    ):
        # print(f"Init is called")
        self.name = name
        self.primitive = primitive
        self.lock = lock
        self.spec = spec

    def __call__(self, val):
        pass

    def __repr__(self):
        return self.name

    def __str__(self):
        return repr(self)


URL = Definition(name="URL", primitive="str", lock=True)

# print(URL0==URL)
# ss = type("url",("Dict[str,Any]",),{})
def type_test(obj: "URL"):
    return 1


# typechecks
aa = "aa"
user_a = type_test(URL(aa))
print(user_a)
# does not typecheck; an int is not a UserId
# user_b = get_user_name(-1)
