Feature: Network checks

Background:
  Given a host defined in env BEHAVE_HOST

Scenario Outline: At ip specific ports are closed
  Given I can ping the host
  When I check port <port>
  Then The port is closed
  Examples: port
  | port |
  | 80   |
  | 22   |
  | 8080 |

