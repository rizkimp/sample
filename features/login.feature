Feature: smoke testing arena
	Scenario: login arena
		Given go to arena homepage
    When  login with tahugoreng and 12345678
    Then 	direct to homepage users

	Scenario: set vip and unset vip
		Given go to manage arena page
		When 	click button create vip
		Then 	create vip popup is shown
		When 	user input passkey & clue and click save
		Then 	the arena become vip
