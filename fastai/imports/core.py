import csv, gc, gzip, os, pickle, shutil, sys, warnings,  io, subprocess
import math, numpy as np, random
import abc, collections, hashlib, itertools, json, operator, pathlib
import mimetypes, inspect, typing, functools, importlib, weakref
import html, re, tarfile, numbers, tempfile

from abc import abstractmethod, abstractproperty
from collections import abc,  Counter, defaultdict, Iterable, namedtuple, OrderedDict
import concurrent
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
from copy import copy, deepcopy
from dataclasses import dataclass, field, InitVar
from enum import Enum, IntEnum
from functools import partial, reduce
from pdb import set_trace
from numpy import array, cos, exp, log, sin, tan, tanh
from operator import attrgetter, itemgetter
from pathlib import Path
from warnings import warn
from contextlib import contextmanager
# from fastprogress.fastprogress import MasterBar, ProgressBar
from io import BufferedWriter, BytesIO

import pkg_resources
# pkg_resources.require("fastprogress>=0.1.19")
# from fastprogress.fastprogress import master_bar, progress_bar

#for type annotations
from numbers import Number
from typing import Any, AnyStr, Callable, Collection, Dict, Hashable, Iterator, List, Mapping, NewType, Optional
from typing import Sequence, Tuple, TypeVar, Union
from types import SimpleNamespace

def try_import(module):
    "Try to import `module`. Returns module's object on success, None on failure"
    try: return importlib.import_module(module)
    except: return None

def have_min_pkg_version(package, version):
    "Check whether we have at least `version` of `package`. Returns True on success, False otherwise."
    try:
        pkg_resources.require(f"{package}>={version}")
        return True
    except:
        return False
