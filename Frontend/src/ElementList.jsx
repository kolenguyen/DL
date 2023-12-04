import React, { useState } from 'react';
import { TextField, Button, List, ListItem, ListItemText } from '@mui/material';
import { makeStyles } from '@mui/styles';

const useStyles = makeStyles((theme) => ({
  container: {
    backgroundColor: 'grey', // Background color
    padding: theme.spacing(2), // Add some padding
    borderRadius: '8px', // Rounded corners
    width: 310,
  },
  button: {
    margin: theme.spacing(4),
  },
  textfield: {
    margin: theme.spacing(2), 
  },

}));

const initialElements = [
  'Element 1',
  'Element 2',
  'Element 3',
  'Element 4',
  'Element 5',
  'Element 6',
  'Element 7',
];

const ElementList = () => {
  const classes = useStyles();
  const [searchTerm, setSearchTerm] = useState('');
  const [filteredElements, setFilteredElements] = useState(initialElements);

  const handleSearch = () => {
    const filtered = initialElements.filter(element =>
      element.toLowerCase().includes(searchTerm.toLowerCase())
    );
    setFilteredElements(filtered);
  };

  const handleReset = () => {
    setSearchTerm('');
    setFilteredElements(initialElements);
  };

  return (
    <div className={classes.container}>
      <TextField
        className={classes.textfield}
        label="Search Elements"
        variant="outlined"
        value={searchTerm}
        onChange={(e) => setSearchTerm(e.target.value)}
      />
      <Button
        className={classes.button}
        variant="contained"
        color="primary"
        onClick={handleSearch}
      >
        Search
      </Button>
      <Button
        className={classes.button}
        variant="contained"
        color="primary"
        onClick={handleReset}
      >
        Reset
      </Button>
      <List>
        {filteredElements.map((element, index) => (
          <ListItem key={index}>
            <ListItemText primary={element} />
          </ListItem>
        ))}
      </List>
    </div>
  );
};

export default ElementList;