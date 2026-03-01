import { useEffect, useState } from 'react';

const endpoint = process.env.REACT_APP_CODESPACE_NAME
  ? `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/teams/`
  : 'http://localhost:8000/api/teams/';

function normalizeResponse(payload) {
  if (Array.isArray(payload)) {
    return payload;
  }

  if (payload && Array.isArray(payload.results)) {
    return payload.results;
  }

  return [];
}

function Teams() {
  const [teams, setTeams] = useState([]);
  const [search, setSearch] = useState('');
  const [isModalOpen, setIsModalOpen] = useState(false);

  const fetchTeams = async () => {
    console.log('Teams endpoint:', endpoint);
    const response = await fetch(endpoint);
    const data = await response.json();
    console.log('Teams fetched data:', data);
    setTeams(normalizeResponse(data));
  };

  useEffect(() => {
    fetchTeams();
  }, []);

  const filteredTeams = teams.filter((team) =>
    JSON.stringify(team).toLowerCase().includes(search.toLowerCase())
  );

  return (
    <>
      <div className="card shadow-sm octofit-card">
        <div className="card-header bg-white d-flex justify-content-between align-items-center">
          <h2 className="h4 mb-0">Teams</h2>
          <button type="button" className="btn btn-outline-primary btn-sm" onClick={() => setIsModalOpen(true)}>
            Details
          </button>
        </div>
        <div className="card-body">
          <div className="d-flex flex-wrap gap-3 align-items-end mb-3">
            <form className="row g-2 flex-grow-1" onSubmit={(event) => event.preventDefault()}>
              <div className="col-sm-8 col-md-6">
                <label htmlFor="teamsSearch" className="form-label">Search teams</label>
                <input
                  id="teamsSearch"
                  className="form-control"
                  value={search}
                  onChange={(event) => setSearch(event.target.value)}
                  placeholder="Filter rows"
                />
              </div>
              <div className="col-sm-4 col-md-3 d-flex align-items-end">
                <button type="button" className="btn btn-primary w-100" onClick={fetchTeams}>Refresh</button>
              </div>
            </form>
            <a className="link-primary" href={endpoint} target="_blank" rel="noreferrer">Open API endpoint</a>
          </div>

          <div className="table-responsive">
            <table className="table table-striped table-hover align-middle octofit-table mb-0">
              <thead className="table-light">
                <tr>
                  <th scope="col">#</th>
                  <th scope="col">Name</th>
                  <th scope="col">Description</th>
                  <th scope="col">Created At</th>
                </tr>
              </thead>
              <tbody>
                {filteredTeams.map((team, index) => (
                  <tr key={team.id}>
                    <td>{index + 1}</td>
                    <td>{team.name ?? '-'}</td>
                    <td>{team.description ?? '-'}</td>
                    <td>{team.created_at ?? '-'}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </div>
      </div>

      <div className={`modal fade ${isModalOpen ? 'show d-block' : ''}`} tabIndex="-1" role="dialog" aria-hidden={!isModalOpen}>
        <div className="modal-dialog modal-dialog-centered" role="document">
          <div className="modal-content">
            <div className="modal-header">
              <h3 className="modal-title h5">Teams Summary</h3>
              <button type="button" className="btn-close" onClick={() => setIsModalOpen(false)} aria-label="Close" />
            </div>
            <div className="modal-body">
              <p className="mb-0">Loaded teams: <strong>{teams.length}</strong></p>
            </div>
            <div className="modal-footer">
              <button type="button" className="btn btn-secondary" onClick={() => setIsModalOpen(false)}>Close</button>
            </div>
          </div>
        </div>
      </div>
      {isModalOpen && <div className="modal-backdrop fade show octofit-modal-backdrop" />}
    </>
  );
}

export default Teams;
