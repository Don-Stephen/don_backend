Feature: {{ description }}
  In order {{ finality }}
  As {{ who }}
  I want {{ purpose }}
​
  Background:
	Given {{ given }}
{% for bgiven in bgivens %}
    And {{ bgiven }}
{% endfor %}

  @tag1 @tag2
  Scenario: {{ title }}
    Given {{ given }}

{% for addgiven in extragivens %}
	And {{ addgiven }}
{% endfor %}

	When {{ when }}
{% for addwhen in extrawhens %}
	And {{ addwhen }}
{% endfor %}
	Then {{ then }}
{% for addthen in extrathens %}
	And {{ addthen }}
{% endfor %}
