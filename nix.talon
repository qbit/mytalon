tag: /terminal/

nix packages:
	insert("cd ~/src/nixpkgs\n")


# nixpkgs-review
review <number_small>:
	insert("nixpkgs-review pr ")
	insert(number_small)
post results:
	insert("nixpkgs-review post-result\n")
