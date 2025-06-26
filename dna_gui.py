from tkinter import *
from tkinter import messagebox

from main import *
from printers import *
from dna_generator import *

# This is the main tkinter program, displaying the shop
def tk_main():

	# Create the main window
	main_root = Tk()

	# We create the new frame (whose parent is root),
	# and additionally the sub-frames (whose parent is the new frame)
	# that will hold the sequences and buttons
	mainFrame = Frame(main_root)
	mainFrame.grid(row = 0, column = 0)
	sequencesFrame = Frame(mainFrame)
	sequencesFrame.grid(row = 0, column = 0)
	legendFrame = Frame(mainFrame)
	legendFrame.grid(row=0, column=1)
	buttonsFrame = Frame(mainFrame)
	buttonsFrame.grid(row = 1, column = 0)
	geneWindowFrame = Frame(mainFrame)
	geneWindowFrame.grid(row = 1, column = 1)

	# Create the sequence label frame and populate with labels
	sequenceLabelFrame = Frame(sequencesFrame)
	sequenceLabelFrame.grid(row=0, column=0)

	motherALabel = Label(sequenceLabelFrame, justify= RIGHT,
						 text = "Mother Chromosome A : ")
	motherALabel.grid(row = 0, column = 0, sticky=E)
	motherBLabel = Label(sequenceLabelFrame, justify= RIGHT,
						 text = "Mother Chromosome B : ")
	motherBLabel.grid(row = 1, column = 0, sticky=E)

	fatherALabel = Label(sequenceLabelFrame, justify= RIGHT,
						 text= "Father Chromosome A : ")
	fatherALabel.grid(row=2, column=0, sticky=E)
	fatherBLabel = Label(sequenceLabelFrame, justify= RIGHT,
						 text= "Father Chromosome B : ")
	fatherBLabel.grid(row=3, column=0, sticky=E)

	childALabel = Label(sequenceLabelFrame, justify= RIGHT,
						 text= "Child Chromosome A : ")
	childALabel.grid(row=4, column=0, sticky=E)
	childBLabel = Label(sequenceLabelFrame, justify= RIGHT,
						 text= "Child Chromosome B : ")
	childBLabel.grid(row=5, column=0, sticky=E)

	# Create the sequence display frame and populate with labels
	sequenceDisplayFrame = Frame(sequencesFrame)
	sequenceDisplayFrame.grid(row=0, column=1)

	motherASequence = Label(sequenceDisplayFrame, justify= RIGHT,
						 text="")
	motherASequence.grid(row=0, column=0, sticky=E)
	motherBSequence = Label(sequenceDisplayFrame, justify= RIGHT,
						 text="")
	motherBSequence.grid(row=1, column=0, sticky=E)

	fatherASequence = Label(sequenceDisplayFrame, justify= RIGHT,
						 text="")
	fatherASequence.grid(row=2, column=0, sticky=E)
	fatherBSequence = Label(sequenceDisplayFrame, justify= RIGHT,
						 text="")
	fatherBSequence.grid(row=3, column=0, sticky=E)

	childASequence = Label(sequenceDisplayFrame, justify= RIGHT,
						 text="")
	childASequence.grid(row=4, column=0, sticky=E)
	childBSequence = Label(sequenceDisplayFrame, justify= RIGHT,
						 text="")
	childBSequence.grid(row=5, column=0, sticky=E)

	update_sequences(sequenceDisplayFrame)

	generateButton = Button(buttonsFrame, text = "Generate New Sequence",
							bg = "White", fg = "Blue",
							command = lambda: update_sequences(sequenceDisplayFrame)
							)
	generateButton.grid(row = 0, column = 2)

	# This is a new window so the mainloop() is now absolutely necessary!
	main_root.mainloop()


def update_sequences(sequenceDisplayFrame):

	labels = get_labels_from_frame(sequenceDisplayFrame)

	allSequences = get_all_sequences("5")
	for i, label in enumerate(labels):
		label.config(text = allSequences[i])

def update_sequences_colour(sequenceDisplayFrame):

	labels = get_labels_from_frame(sequenceDisplayFrame)

	allSequences = get_all_sequences("5")
	for i, label in enumerate(labels):
		if i < 4:
			label.config(text= tkinter_sequence_printer(allSequences[i], True))
		else:
			parent_dna = [allSequences[0], allSequences[1],
						  allSequences[2], allSequences[3]]

			# Create a Text widget to simulate a multi-colored label
			text_widget = Text(label, height=3, width=30, bg="white", bd=0, highlightthickness=0)
			text_widget.grid(row=0, column=0, padx=10, pady=10)

			# Insert text with different colors
			text_widget.insert("1.0", "This is ")  # Line 1, column 0
			text_widget.insert("1.7", "red", "red_tag")
			text_widget.insert("1.10", ", ")
			text_widget.insert("1.12", "blue", "blue_tag")
			text_widget.insert("1.16", ", and ")
			text_widget.insert("1.22", "green", "green_tag")

			# Configure tags for colors
			text_widget.tag_configure("red_tag", foreground="red")
			text_widget.tag_configure("blue_tag", foreground="blue")
			text_widget.tag_configure("green_tag", foreground="green")
			label.config(text=tkinter_sequence_printer(allSequences[i], True))

# Lots of tab/space errors. not fully implemented. dictionaries need to inform colours above
def tkinter_colour_printer(dna, withColour=False, parentDNA = None):

	# Defines the length of the encoding for all genes using the
    # longest gene present.
    encoder = getNumberOfEncodedBases()

	# Define the number of bases that have been read (the counter)
    basesRead = 0

	# define the end of base character
    end = " - "

	# Create the coloured string to return
    colouredDictionaries = []
	geneCluster = None

	# Loop through all gene clusters (collection of genes) to be used
    for geneClusterLabel in genesUsed:
		geneCluster = genesUsed[geneClusterLabel]

		# Check whether the sequence should be printed with colours
		if withColour:
			colouredDictionaries.append({"Colour": "yellow",
										 "Bases": dna[basesRead],
										 "End": end})
			colouredDictionaries.append({"Colour": "green",
										 "Bases": dna[basesRead + 1: basesRead + encoder],
										 "End": " - "
										 })
		else:
			colouredDictionaries.append({"Colour": "black",
										 "Bases": dna[basesRead],
										 "End": end
										 })
			colouredDictionaries.append({"Colour": "black",
										 "Bases": dna[basesRead + 1: basesRead + encoder],
										 "End": end
										 })

		# After the encoding has been read increase the value of bases read
		basesRead += encoder

		# Loop through all genes within the geneCluster
        for gene in geneCluster:

			# Check how many bases long the current gene is
            basesToRead = len(list(geneCluster[gene].keys())[0])
			geneColour = ""

			# If the user has specified to print with colour, and the
            # list of parent chromosomes is 4 chromosomes long
            if withColour and (len(parentDNA) == 4):

				# Check if the current gene exists in either chromosome
                # of either parent and set the colour accordingly
                geneColour = fun.checkGeneMatchesParent(dna[basesRead: basesRead + basesToRead],
                                                    parentDNA[0][basesRead: basesRead + basesToRead],
                                                    parentDNA[1][basesRead: basesRead + basesToRead],
                                                    parentDNA[2][basesRead: basesRead + basesToRead],
                                                    parentDNA[3][basesRead: basesRead + basesToRead])

				if geneColour == "B":
					geneColour = "purple"
				elif geneColour == "M":
					geneColour = "red"
				elif geneColour == "F":
					geneColour = "blue"
				elif geneColour == "N":
					geneColour = "black"

			# If the end of the dna has been reached print without seperator
            if (basesRead + basesToRead) == len(dna):
				colouredDictionaries.append({"Colour": geneColour,
											 "Bases": dna[basesRead: basesRead + basesToRead],
											 "End": ""
											 })
			else:
				colouredDictionaries.append({"Colour": geneColour,
											 "Bases": dna[basesRead: basesRead + basesToRead],
											 "End": end
											 })
			# Update the value of bases read at the end of the loop
            basesRead += basesToRead

	return colouredDictionaries

def get_labels_from_frame(frame):
	# Get all children of the frame and filter for Labels
	labels = ([widget for widget in frame.winfo_children()
			   if isinstance(widget, Label)])
	return labels

def get_all_sequences(numberOfGenes):
	# Randomly create two chromosomes for the mother and father
	motherChromosomeA, motherChromosomeB = gen.BuildSequenceFromGenes(numberOfGenes)
	fatherChromosomeA, fatherChromosomeB = gen.BuildSequenceFromGenes(numberOfGenes)

	# Run the Signal Switching method to create two child chromosomes
	childChASignal, childChBSignal = SignalSwitching(motherChromosomeA,
													 motherChromosomeB,
													 fatherChromosomeA,
													 fatherChromosomeB)
	allSequences = [motherChromosomeA, motherChromosomeB,
					fatherChromosomeA, fatherChromosomeB,
					childChASignal, childChBSignal]
	return allSequences

# This is the purchase function which handles whether a purchase can be made
# I don't like the fact we passes tableFrame into a method where it is largely
# irrelevant, so I will fix this in the decoupled-multiple-file program I make
def purchase(user_input):

	# As these are global we no longer need to pass them as parameters
	global items
	global totalSales
	try:
		key = int(user_input)

		if items[key]["Stock"] > 0:
			items[key]["Stock"] -= 1
			totalSales += items[key]["Price"]

			# NOTE instead of updating the stock here, the lambda function
			# has chaged to only do that if purchase() returns True
			return True
		else:
			messagebox.showwarning("Out of Stock!", "Out of Stock")
			return False

	except (ValueError, KeyError):
		messagebox.showwarning("Enter a Valid Key!", "Enter a Valid Key!")
		return False



# This is update stock function that populates the table based on our items dictionary
# It now also updates the totalSales in the GUI
def update_stock(tableFrame, salesValue):

	# Again, this function may access our global variables,
	# so we haven't passed them as parameters
	global items
	global totalSales

	# This fills in our table as before, we have passed the tableFrame as a parameter
	# as we do not need the Header Labels, just to add below them
	for i, item in enumerate(items):
		idLabel = Label(tableFrame, text = item).grid(row = i + 1, column = 0)
		nameLabel = Label(tableFrame, text = items[item]["Name"]).grid(row = i + 1, column = 1)
		priceLabel = Label(tableFrame, text = items[item]["Price"]).grid(row = i + 1, column = 2)
		quantityLabel = Label(tableFrame, text = items[item]["Stock"]).grid(row = i + 1, column = 3)

	# This updates the totalSales by editing the salesValue label
	salesValue.config(text = str(f"{totalSales:.2f}"))



# This is the load stock function that is currenty hardcoded
# - you can replace this to load from file (you will need a separate write to file)
def load_stock():
	items = {

			1: {"Name" : "Ben Shaw's D&B",
			  	"Price": 1.20,
			  	"Stock": 20
				},
			2: {"Name" : "Coca Cola",
			  	"Price": 1.50,
			  	"Stock": 100
				},
			3: {"Name" : "Irn Bru",
			  	"Price": 0.99,
			  	"Stock": 32
				},
			4: {"Name" : "R. White's Lemonade",
			  	"Price": 1.20,
			  	"Stock": 57
				}
			}

	return items


# We define desired global variables as such. Now they can be accessed
# anywhere at any time! Dangerous, but easier...
# Beware because: 1) easier to cause problems
#				  2) harder to debug
#				  3) WJEC *may* not like it
global items
global totalSales

# We initialise our now global variables as usual
items = load_stock()
totalSales = 0

# NOTE That at this point we could also create both windows,
# and leave main unpopulated until after login...

# We kick off our program by calling the login function
tk_main()
