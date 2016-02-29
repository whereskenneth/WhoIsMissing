import os
import tempfile


def before_all(context):
    context.tmp_dir = tempfile.TemporaryDirectory(dir=os.path.abspath(os.path.curdir))
    context.old_injection_files = []

def after_all(context):
    pass
    # context.tmp_dir.cleanup()


def before_tag(context, tag):
    pass


def after_tag(context, tag):
    pass


def before_feature(context, feature):
    pass


def after_feature(context, feature):
    pass


def before_scenario(context, scenario):
    pass


def after_scenario(context, scenario):
    pass


def before_step(context, step):
    pass


def after_step(context, step):
    pass
