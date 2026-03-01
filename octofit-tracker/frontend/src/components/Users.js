import { useEffect, useState } from 'react';

const endpoint = process.env.REACT_APP_CODESPACE_NAME
  ? `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/users/`
  : 'http://localhost:8000/api/users/';

function normalizeResponse(payload) {
  if (Array.isArray(payload)) {
    return payload;
  }

  if (payload && Array.isArray(payload.results)) {
    return payload.results;
  }

  return [];
}

function Users() {
  const [users, setUsers] = useState([]);
  const [search, setSearch] = useState('');
  const [isModalOpen, setIsModalOpen] = useState(false);

  const fetchUsers = async () => {
    console.log('Users endpoint:', endpoint);
    const response = await fetch(endpoint);
    const data = await response.json();
    console.log('Users fetched data:', data);
    setUsers(normalizeResponse(data));
  };

  useEffect(() => {
    fetchUsers();
  }, []);

  const filteredUsers = users.filter((user) =>
    JSON.stringify(user).toLowerCase().includes(search.toLowerCase())
  );

  return (
    <>
      <div className="card shadow-sm octofit-card">
        <div className="card-header bg-white d-flex justify-content-between align-items-center">
          <h2 className="h4 mb-0">Users</h2>
          <button type="button" className="btn btn-outline-primary btn-sm" onClick={() => setIsModalOpen(true)}>
            Details
          </button>
        </div>
        <div className="card-body">
          <div className="d-flex flex-wrap gap-3 align-items-end mb-3">
            <form className="row g-2 flex-grow-1" onSubmit={(event) => event.preventDefault()}>
              <div className="col-sm-8 col-md-6">
                <label htmlFor="usersSearch" className="form-label">Search users</label>
                <input
                  id="usersSearch"
                  className="form-control"
                  value={search}
                  onChange={(event) => setSearch(event.target.value)}
                  placeholder="Filter rows"
                />
              </div>
              <div className="col-sm-4 col-md-3 d-flex align-items-end">
                <button type="button" className="btn btn-primary w-100" onClick={fetchUsers}>Refresh</button>
              </div>
            </form>
            <a className="link-primary" href={endpoint} target="_blank" rel="noreferrer">Open API endpoint</a>
          </div>

          <div className="table-responsive">
            <table className="table table-striped table-hover align-middle octofit-table mb-0">
              <thead className="table-light">
                <tr>
                  <th scope="col">#</th>
                  <th scope="col">User Ref</th>
                  <th scope="col">Team Ref</th>
                  <th scope="col">Age</th>
                  <th scope="col">Fitness Goal</th>
                </tr>
              </thead>
              <tbody>
                {filteredUsers.map((user, index) => (
                  <tr key={user.id}>
                    <td>{index + 1}</td>
                    <td>{user.user ?? user.name ?? '-'}</td>
                    <td>{user.team ?? '-'}</td>
                    <td>{user.age ?? '-'}</td>
                    <td>{user.fitness_goal ?? '-'}</td>
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
              <h3 className="modal-title h5">Users Summary</h3>
              <button type="button" className="btn-close" onClick={() => setIsModalOpen(false)} aria-label="Close" />
            </div>
            <div className="modal-body">
              <p className="mb-0">Loaded users: <strong>{users.length}</strong></p>
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

export default Users;
