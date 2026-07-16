def display_radha_krishna_cli():
    # Multi-line string holding the ASCII representation
    ascii_art = """
                           .---.
                          /     \\

                         |  (O)  |       _
                          \\     /      /   \\
                           `---'      |  *  |
                             |         \\ _ /
                            / \\          |
                           /   \\        / \\
       ___________________/_____\\______/___\\___________________

      |                                                        |
      |     .-''''-.                .-''''-.                   |
      |    /        \\              /        \\                  |
      |   |   __    _|            |   __    _|                 |
      |   |  (  )  ( )            |  (  )  ( )                 |
      |   |   `""  `"             |   `""  `"                  |
      |    \\     \\_               \\     \\_                 |
      |     \\  '--'                \\  '--'                 |
      |      '-____.-'              '-____.-'                  |
      |        /   \\                  /   \\                    |
      |       /     \\                /     \\                   |
      |________________________________________________________|
         ||   ||      ( )     ( )     ( )      ||   ||   ||
         ||   ||       |       |       |       ||   ||   ||
    =======''===''====(O)=====(O)=====(O)======''===''===''======
                      [=================]   <- Divine Flute ->
    """
    
    # ANSI escape code for bright yellow/gold text
    gold_color = "\033[93m"
    reset_color = "\033[0m"
    
    print(gold_color + ascii_art + reset_color)
    print("✨ Jay Shree Radha Krishna ✨".center(64))

if __name__ == "__main__":
    display_radha_krishna_cli()
