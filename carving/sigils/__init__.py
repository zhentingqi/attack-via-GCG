"""Implements the nitty-gritty of various objectives.

Note that these imports are 'specialized implementations' for one of these attack objectives like harm or extraction.
For many attacks, not specialized implementation is necessary. The files do not
contain exhaustive lists of all attacks. """

from .generic_sigils import FixedTargetSigil, FixedCollisionSigil, ContextTargetSigil, ContextCollisionSigil, ContextMultipleTargetsSigil
from .meta_sigils import AbjurationSigilForContextTargetSigil

# Category: Extraction
from .extraction_sigils import RepeaterSigil, SystemRepeaterSigil, ReverserSigil
# Category: Control
from .control_sigils import SpecialTokenContextTargetSigil, DividerSigil, MagnetSigil
# Category: Misdirection
from .misdirection_sigils import GoodAssistantSigil
# Category: Denial of Service
from .dos_sigils import FixedNaNSigil, FixedActNaNSigil, DDOSSigil, FixedAttackRepeaterSigil, AttackRepeaterSigil
# Category: Jailbreak
from .harmful_sigils import AlienateSigil, UnalignmentSigil

implementation_lookup = {
    "repeater": RepeaterSigil,  #! I care about this one
    "sysrepeater": SystemRepeaterSigil,
    "attackrepeater": AttackRepeaterSigil,
    "reverser": ReverserSigil,
    "fixed_target": FixedTargetSigil,
    "fixed_collision": FixedCollisionSigil,
    "fixed_selfrep": FixedAttackRepeaterSigil,
    "target_in_context": ContextTargetSigil,
    "multiple_targets_in_context": ContextMultipleTargetsSigil,
    "special_target_in_context": SpecialTokenContextTargetSigil,
    "collision_in_context": ContextCollisionSigil,
    "alienate": AlienateSigil,
    "ddos": DDOSSigil,
    "nanlogitattack": FixedNaNSigil,
    "nanactattack": FixedActNaNSigil,
    "good_assistant": GoodAssistantSigil,
    "divider": DividerSigil,
    "magnet": MagnetSigil,
    "harm_abjuration": AbjurationSigilForContextTargetSigil,
    "unaligner": UnalignmentSigil,
}


def construct(model, tokenizer, config, aux_models, cache_dir=None):
    sigil = implementation_lookup[config["sigil_type"]](model, tokenizer, aux_models, cache_dir=cache_dir, **config)
    return sigil
