Feature: {{ description }}
  In order {{ finality }}
  As {{ who }}
  I want {{ purpose }}
​
  Background:
	Given {{ bgiven.content }}
{% for bgiven in bgivens %}
    And {{ bgiven.content }}
{% endfor %}

  @tag1 @tag2
  Scenario: {{ title }}
    Given {{ sgiven.content }}

{% for addgiven in extragivens %}
	And {{ addgiven.content }}
{% endfor %}

	When {{ when.content }}
{% for addwhen in extrawhens %}
	And {{ addwhen.content }}
{% endfor %}
	Then {{ then.content }}
{% for addthen in extrathens %}
	And {{ addthen.content }}
{% endfor %}
