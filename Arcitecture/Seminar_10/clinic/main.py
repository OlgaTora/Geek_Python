import uvicorn

from Arcitecture.Seminar_10.clinic.database.prepare_schema import PrepareDatabase

if __name__ == '__main__':
    create_db = PrepareDatabase()
    create_db.prepare_db()
    uvicorn.run(
        'services.app:app',
        host='127.0.0.1',
        port=8000,
        log_level='debug',
        reload=True
    )
