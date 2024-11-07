import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom'

import GlobalStyles from './styles/GlobalStyles'
import AppLayout from './ui/AppLayout'

import Dashboard from './pages/Dashboard'

function App() {
  return (
    <>
      <GlobalStyles />
      <BrowserRouter>
        <Routes>
          <Route element={<AppLayout />}>
            <Route index element={<Navigate replace to='dashboard' />}/>
            <Route path='dashboard' element={<Dashboard />} />
          </Route>
        </Routes>
      </BrowserRouter>
    </>
  )
}

export default App