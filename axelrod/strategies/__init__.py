from ..player import is_basic, obey_axelrod
from ._strategies import *

# `from ._strategies import *` import the collection `strategies`
# Now import the Meta strategies. This cannot be done in _strategies
# because it creates circular dependencies

from .meta import (
    MetaPlayer, MetaMajority, MetaMinority, MetaWinner, MetaHunter,
    MetaMajorityMemoryOne, MetaWinnerMemoryOne, MetaMajorityFiniteMemory,
    MetaWinnerFiniteMemory, MetaMajorityLongMemory, MetaWinnerLongMemory,
    MetaMixer
    )

recursive_strategies = [MetaHunter, MetaMajority, MetaMinority, MetaWinner,
                   MetaMajorityMemoryOne, MetaWinnerMemoryOne,
                   MetaMajorityFiniteMemory, MetaWinnerFiniteMemory,
                   MetaMajorityLongMemory, MetaWinnerLongMemory, MetaMixer]
all_strategies.extend(recursive_strategies)

# Distinguished strategy collections in addition to
# `all_strategies` from _strategies.py

demo_strategies = [Cooperator, Defector, TitForTat, Grudger, Random]
basic_strategies = [s for s in all_strategies if is_basic(s())]
strategies = [s for s in all_strategies if obey_axelrod(s())]
#ordinary_strategies = strategies  # This is a legacy and will be removed
cheating_strategies = [s for s in strategies if not obey_axelrod(s())]
