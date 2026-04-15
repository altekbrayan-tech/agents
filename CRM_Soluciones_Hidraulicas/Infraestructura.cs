 Aquí tienes el contenido completo para los archivos solicitados en tu proyecto CRM_Soluciones_Hidraulicas_Backend:

--- ARCHIVO: Models/Entities.cs ---
```csharp
using System;
using System.Collections.Generic;
using Microsoft.EntityFrameworkCore;

namespace SolutionsHydraulic.Models
{
    public enum TaskStatus { Pendiente, EnCamino, EnEjecucion, EnRevision, Finalizada, Cancelada }

    public class ResidentialUnit
    {
        public int Id { get; set; }
        public string NIT { get; set; }
        public string Nombre { get; set; }
        public string Direccion { get; set; }
        public string Telefono { get; set; }
        public string EmailAdmin { get; set; }
    }

    public class Contract
    {
        public int Id { get; set; }
        public int UnitId { get; set; }
        public decimal PrecioBase { get; set; }
        public decimal IpcIncremento { get; set; }
        public DateTime UltimoAumento { get; set; }
    }

    public class WorkTask
    {
        public int Id { get; set; }
        public int UnitId { get; set; }
        public string TecnicoId { get; set; }
        public TaskStatus Estado { get; set; }
        public string Descripcion { get; set; }
        public DateTime FechaProgramada { get; set; }
    }
}
```

--- ARCHIVO: Data/ApplicationDbContext.cs ---
```csharp
using Microsoft.EntityFrameworkCore;

namespace SolutionsHydraulic.Data
{
    public class ApplicationDbContext : DbContext
    {
        public ApplicationDbContext(DbContextOptions<ApplicationDbContext> options) : base(options) { }

        public DbSet<Models.ResidentialUnit> ResidentialUnits { get; set; }
        public DbSet<Models.Contract> Contracts { get; set; }
        public DbSet<Models.WorkTask> WorkTasks { get; set; }

        protected override void OnModelCreating(ModelBuilder modelBuilder)
        {
            base.OnModelCreating(modelBuilder);

            modelBuilder.Entity<Models.ResidentialUnit>()
                .Property(r => r.NIT)
                .IsRequired();

            modelBuilder.Entity<Models.Contract>()
                .HasIndex(c => c.UnitId)
                .IsUnique();

            modelBuilder.Entity<Models.WorkTask>()
                .Property(t => t.Estado)
                .HasConversion<string>();
        }
    }
}
```

--- ARCHIVO: Controllers/ConjuntosController.cs ---
```csharp
using Microsoft.AspNetCore.Mvc;
using SolutionsHydraulic.Data;
using System.Linq;

namespace SolutionsHydraulic.Controllers
{
    [ApiController]
    [Route("conjuntos")]
    public class ConjuntosController : ControllerBase
    {
        private readonly ApplicationDbContext _context;

        public ConjuntosController(ApplicationDbContext context)
        {
            _context = context;
        }

        [HttpGet]
        public IActionResult ListarConjuntos()
        {
            var conjuntos = _context.ResidentialUnits.ToList();
            return Ok(conjuntos);
        }

        [HttpPost]
        public IActionResult CrearConjunto([FromBody] Models.ResidentialUnit unit)
        {
            _context.ResidentialUnits.Add(unit);
            _context.SaveChanges();
            return CreatedAtAction(nameof(ListarConjuntos), new { id = unit.Id }, unit);
        }

        [HttpPut("aplicar-ipc/{id}")]
        public IActionResult AplicarIpc([FromRoute] int id, [FromBody] decimal porcentaje)
        {
            var contract = _context.Contracts.Find(id);
            if (contract == null) return NotFound();

            contract.PrecioBase *= (1 + porcentaje / 100);
            _context.SaveChanges();
            return NoContent();
        }
    }
}
```

Este contenido incluye el espacio de nombres, las entidades, el contexto de base de datos y el controlador completo, listo para ser copiado y pegado en sus respectivos archivos.