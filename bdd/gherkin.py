from django.template import loader
from django.core.files.base import ContentFile

from bdd.models import Feature
from bdd.serializers import FeatureSerializer

class Gherkin(object):
    def __init__(self, feature):
        self.feature = feature

    def compose(self):
        data = {}
        serializer = FeatureSerializer(self.feature)
        data.update(serializer.data)
        data["background"] = self.compose_background()
        data["scenarios"] = self.compose_scenario()
        return data

    def compose_scenario(self):
        scenarios = []
        for scenario in self.feature.scenarios.all():
            data = {}
            givens = list(scenario.givens.all())
            whens = list(scenario.whens.all())
            thens = list(scenario.thens.all())
            if len(givens) > 0:
                data['sgiven'] = givens.pop(0)
            if len(whens) > 0:
                data['when'] = whens.pop(0)
            if len(thens) > 0:
                data['then'] = thens.pop(0)
            data["title"] = scenario.title
            data.update({"extragivens": givens, "extrawhens": whens,
                         "extrathens": thens})
            scenarios.append(data)
        return scenarios

    def compose_background(self):
        background = self.feature.background
        if background is not None:
            data = {}
            data.update({'bgiven': background.givens.pop(0)})
            data.update({'bgivens': background.givens})
        else:
            data = None
        return data

    def render_template(self):
        template = loader.get_template('bdd/base.feature')
        return template.render(self.compose())

    def write_file(self):
        f = ContentFile(name='{project}_{feature}.feature'.format(feature=self.feature.id,
                                                                  project=self.feature.project.id),
                        content=self.render_template())
                                                   
        self.feature.ffile = f
        self.feature.save()
