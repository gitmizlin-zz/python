#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Me-page, presentation of Mi.

"""

# Store my ascii image in a separat variabel as a raw string
meImage = r"""
             *     ,MMM8&&&.            *
                  MMMM88&&&&&    .
                 MMMM88&&&&&&&
     *           MMM88&&&&&&&&
                 MMM88&&&&&&&&
                 'MMM88&&&&&&'
                   'MMM8&&&'      *
          |\___/|
          )     (             .              '
         =\     /=
           )===(       *
          /     \
          |     |
         /       \
         \       /
  _/\_/\_/\__  _/_/\_/\_/\_/\_/\_/\_/\_/\_/\_
  |  |  |  |( (  |  |  |  |  |  |  |  |  |  |
  |  |  |  | ) ) |  |  |  |  |  |  |  |  |  |
  |  |  |  |(_(  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
  jgs|  |  |  |  |  |  |  |  |  |  |  |  |  |
"""


print("""
Min Me-sida
==============================================================================

Hej, 

Jag heter Mi och bor i Stockholm.

{image} 

Tidigare har jag studerat webbprogramering lite grann på egen hand men har ingen erfarenhet inom IT området. Hoppas att jag denna kurs blir en bra kick-start för att läsa vidare.

Utöver webbprogramering tilldelar jag mycket tid på att baka, speciellt kaffebröd.

""".format(image=meImage))
