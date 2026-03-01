import './App.css';
import { NavLink, Navigate, Route, Routes } from 'react-router-dom';
import Activities from './components/Activities';
import Leaderboard from './components/Leaderboard';
import Teams from './components/Teams';
import Users from './components/Users';
import Workouts from './components/Workouts';

function App() {
  const navLinkClass = ({ isActive }) =>
    `nav-link text-white ${isActive ? 'fw-bold text-decoration-underline' : ''}`;

  return (
    <div className="app-shell">
      <nav className="navbar navbar-expand-lg navbar-dark bg-primary octofit-navbar">
        <div className="container">
          <span className="navbar-brand octofit-title d-flex align-items-center gap-2">
            <img src="/octofitapp-small.png" alt="OctoFit" className="octofit-logo" />
            OctoFit Tracker
          </span>
          <button
            className="navbar-toggler"
            type="button"
            data-bs-toggle="collapse"
            data-bs-target="#octofitNav"
            aria-controls="octofitNav"
            aria-expanded="false"
            aria-label="Toggle navigation"
          >
            <span className="navbar-toggler-icon" />
          </button>
          <div className="collapse navbar-collapse" id="octofitNav">
            <div className="navbar-nav ms-auto">
              <NavLink className={navLinkClass} to="/users">Users</NavLink>
              <NavLink className={navLinkClass} to="/teams">Teams</NavLink>
              <NavLink className={navLinkClass} to="/activities">Activities</NavLink>
              <NavLink className={navLinkClass} to="/leaderboard">Leaderboard</NavLink>
              <NavLink className={navLinkClass} to="/workouts">Workouts</NavLink>
            </div>
          </div>
        </div>
      </nav>

      <main className="container py-4">
        <Routes>
          <Route path="/" element={<Navigate to="/users" replace />} />
          <Route path="/users" element={<Users />} />
          <Route path="/teams" element={<Teams />} />
          <Route path="/activities" element={<Activities />} />
          <Route path="/leaderboard" element={<Leaderboard />} />
          <Route path="/workouts" element={<Workouts />} />
        </Routes>
      </main>
    </div>
  );
}

export default App;
