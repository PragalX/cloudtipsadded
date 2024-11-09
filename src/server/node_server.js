// server/node_server.js
import express from 'express';

const nodeApp = express();
const PORT = 3001;

// Define a route for Express
nodeApp.get('/node/hello', (req, res) => {
  res.json({ message: 'Node me Ram Ram Bhaay ' });
});

// Start the server
nodeApp.listen(PORT, () => {
  console.log(`Node.js Express server running on http://localhost:${PORT}`);
});
