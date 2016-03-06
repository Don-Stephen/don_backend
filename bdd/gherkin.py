from django.template import loader

from bdd.models import Feature

class Gherkin(object):
    def __init__(self, feature):
        self.feature = feature

    def compose(self):
        data = {}
        #get feature data

        data.update(self.compose_background)
        data.update(self.compose_scenario)
        return data

    def compose_scenario(self):
        # pending several scenarios
        data = {}
        scenario = self.feature.scenario.all()[0]

        # given optional
        givens = scenario.givens.all()
        # when + then same length
        whens = scenario.whens.all()
        thens = scenario.thens.all()

        data.update({"title": scenario.title, "sgiven": givens.pop(0),
                     "when": scenario.pop(0), "then": thens.pop(0)})
        data.update({"extragivens": givens, "extrawhens": whens,
                     "extrathens": thens})
        return data

    def compose_background(self):
        background = self.feature.background
        data = {}
        data.update({'bgiven': background.givens.pop(0)})
        data.update({'bgivens': background.givens})
        return data

    def render_template(self):
        template = loader.get_template('bdd/base.feature')
        return template.render(self.compose())

    def write_file(self):
        pass
