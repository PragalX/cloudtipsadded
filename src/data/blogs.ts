export interface Blog {
  id: string;
  title: string;
  date: string;
  content: string;
}

export const blogs: Blog[] = [
  {
    id: '1',
    title: 'About Love',
    date: '2024-11-08',
    content: 'Love is Cloud Computing...'
  },
  {
    id: '2',
    title: 'The Future of Cloud Computing',
    date: '2024-11-07',
    content: 'As we move towards more distributed systems, the cloud continues to evolve...'
  }
];
