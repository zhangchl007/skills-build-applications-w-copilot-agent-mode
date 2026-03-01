import { useEffect, useState } from 'react';

const endpoint = process.env.REACT_APP_CODESPACE_NAME
  ? `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/activities/`
  : 'http://localhost:8000/api/activities/';

function normalizeResponse(payload) {
  if (Array.isArray(payload)) {
    return payload;
  }

  if (payload && Array.isArray(payload.results)) {
    return payload.results;
  }

  return [];
}

function Activities() {
  const [activities, setActivities] = useState([]);

  useEffect(() => {
    async function fetchActivities() {
      console.log('Activities endpoint:', endpoint);
      const response = await fetch(endpoint);
      const data = await response.json();
      console.log('Activities fetched data:', data);
      setActivities(normalizeResponse(data));
    }

    fetchActivities();
  }, []);

  return (
    <div>
      <h2 className="mb-3">Activities</h2>
      <ul className="list-group">
        {activities.map((activity) => (
          <li key={activity.id} className="list-group-item">
            <strong>{activity.activity_type}</strong>
            {` — ${activity.duration_minutes ?? 0} min`}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default Activities;
