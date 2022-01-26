This project is a command line program which is used to test for catastrophic forgetting.

**Usage**:

- Run the main file
- Use parameter `-l` for giving the name of the database, multiple can be used at once
- When using multiple `-l` parameters, it will go through all possible iterations of the given databases
- Use parameter `-n` for giving the number of layer that you wish to freeze during the learning process
- Multiple `-n` parameters can be used, it will go through the learning process with each `-n` parameter given
- Models are saved in the `/models/model_name` folder
- It creates a .txt file which contains the evaluated results of given models
- The default name of the .txt is `out.txt`