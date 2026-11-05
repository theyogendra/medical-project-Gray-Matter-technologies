import { render, screen } from '@testing-library/react';
import { BrowserRouter } from 'react-router-dom';
import App from './App';
import { AuthProvider } from './context/AuthContext';

describe('App', () => {
  it('renders the base application shell', () => {
    render(
      <BrowserRouter>
        <AuthProvider>
          <App />
        </AuthProvider>
      </BrowserRouter>,
    );

    expect(screen.getByText(/medical portal/i)).not.toBeNull();
  });
});
