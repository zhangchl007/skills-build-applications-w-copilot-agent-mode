import { useEffect, useState } from 'react';

const endpoint = process.env.REACT_APP_CODESPACE_NAME
  ? `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/workouts/`
  : 'http://localhost:8000/api/workouts/';

function normalizeResponse(payload) {
  if (Array.isArray(payload)) {
    return payload;
  }

  if (payload && Array.isArray(payload.results)) {
    return payload.results;
  }

  return [];
}

function Workouts() {
  const [workouts, setWorkouts] = useState([]);

  useEffect(() => {
    async function fetchWorkouts() {
      console.log('Workouts endpoint:', endpoint);
      const response = await fetch(endpoint);
      const data = await response.json();
      console.log('Workouts fetched data:', data);
      setWorkouts(normalizeResponse(data));
    }

    fetchWorkouts();
  }, []);

  return (
    <div>
      <h2 className="mb-3">Workouts</h2>
      <ul className="list-group">
        {workouts.map((workout) => (
          <li key={workout.id} className="list-group-item">
            <strong>{workout.title || 'Workout'}</strong>
            {workout.target_goal ? ` — Goal: ${workout.target_goal}` : ''}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default Workouts;
