Feature: {{ description }}
  In order {{ finality }}
  As {{ who }}
  I want {{ purpose }}

{% if background %}
  Background:
	Given {{ bgiven.content }}
{% for bgiven in bgivens %}
    And {{ bgiven.content }}
{% endfor %}
{% endif %}

{% for scenario in scenarios %}
  @tag1 @tag2
  Scenario: {{ scenario.title }}
    Given {{ scenario.sgiven.content }}

{% for addgiven in scenario.extragivens %}
	And {{ addgiven.content }}
{% endfor %}
	When {{ scenario.when.content }}
{% for addwhen in scenario.extrawhens %}
	And {{ addwhen.content }}
{% endfor %}
	Then {{ scenario.then.content }}
{% for addthen in scenario.extrathens %}
	And {{ addthen.content }}
{% endfor %}

{% endfor %}
