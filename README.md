Patch notes:
1.2
- helper functions both take in a parameter n. I and S now returns a n-length list of ints and strings respectively.

1.1
- added helper functions: S() and I()
  S() and I() are functions that make taking the next input much easier to type (I hate typing out int(next(it))).
  However, this introduced slight overhead to our fast i/o. S() actually directly calls the C method next so it's still blazingly fast,
  but I() is a python lambda definition so our next int input will always cost some extra function call overhead. I was considering
  other configurations, but I think this small price to pay for massive convenience is ok.

1.0 
- the og setup
