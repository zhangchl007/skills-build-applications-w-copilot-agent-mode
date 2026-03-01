import { useEffect, useState } from 'react';

const endpoint = process.env.REACT_APP_CODESPACE_NAME
  ? `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/leaderboard/`
  : 'http://localhost:8000/api/leaderboard/';

function normalizeResponse(payload) {
  if (Array.isArray(payload)) {
    return payload;
  }

  if (payload && Array.isArray(payload.results)) {
    return payload.results;
  }

  return [];
}

function Leaderboard() {
  const [entries, setEntries] = useState([]);

  useEffect(() => {
    async function fetchLeaderboard() {
      console.log('Leaderboard endpoint:', endpoint);
      const response = await fetch(endpoint);
      const data = await response.json();
      console.log('Leaderboard fetched data:', data);
      setEntries(normalizeResponse(data));
    }

    fetchLeaderboard();
  }, []);

  return (
    <div>
      <h2 className="mb-3">Leaderboard</h2>
      <ul className="list-group">
        {entries.map((entry) => (
          <li key={entry.id} className="list-group-item">
            <strong>Rank {entry.rank ?? '-'}</strong>
            {` — Points: ${entry.total_points ?? 0}`}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default Leaderboard;
