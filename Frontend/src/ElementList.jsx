import React, { useState } from 'react';
import { TextField, Button, List, ListItem, ListItemText } from '@mui/material';
import { makeStyles } from '@mui/styles';

const useStyles = makeStyles((theme) => ({
  container: {
    backgroundColor: '#26577C', // Background color
    padding: theme.spacing(2), // Add some padding
    borderRadius: '8px', // Rounded corners
    width: 310,
    color: '#EBE4D1',

  },
  button: {
    margin: theme.spacing(4),
  },
  textfield: {
    margin: theme.spacing(2), 
  },

}));

const initialElements = [
  {title:"Lesson 1",url:"https://www.youtube.com/embed/jCUaMdXsI7w?si=i7lWqrLC2gP6tICo"},
  {title:"Lesson 2",url:"https://www.youtube.com/embed/7suKo9kCTus?si=5Yr1Wp-tHmPpygFZ"},
  {title:"Lesson 3",url:"https://www.youtube.com/embed/qa9qSPsj840?si=iTHnZzc8om3cAPrA"},
  {title:"Lesson 4",url:"https://www.youtube.com/embed/ghQr2hzdx8k?si=5-GRQP-nlOdqmny3"},
  {title:"Lesson 5",url:"https://www.youtube.com/embed/mqG8sWoOsBQ?si=AKtyGgZssVbvDXxM"},
  {title:"Lesson 6",url:"https://www.youtube.com/embed/7suKo9kCTus?si=5Yr1Wp-tHmPpygFZ"},

];

const ElementList = ({ onItemClicked }) => {
  const classes = useStyles();
  const [searchTerm, setSearchTerm] = useState('');
  const [filteredElements, setFilteredElements] = useState(initialElements);

  const handleSearch = () => {
    const filtered = initialElements.filter(element =>
      element.title.toLowerCase().includes(searchTerm.toLowerCase())
    );
    setFilteredElements(filtered);
  };

  const handleReset = () => {
    setSearchTerm('');
    setFilteredElements(initialElements);
  };
  const handleItemClick = (url) => {
    onItemClicked(url);
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
          <ListItem key={index} button onClick={() => handleItemClick(element.url)}>
            <ListItemText primary={element.title} />
          </ListItem>
        ))}
      </List>
    </div>
  );
};

export default ElementList;