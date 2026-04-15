 Aquí tienes el contenido completo para los archivos `ApplicationDbContext.cs` y `ConjuntosController.cs` que has proporcionado:

--- ARCHIVO: Data/ApplicationDbContext.cs ---
```csharp
using Microsoft.EntityFrameworkCore;
using SolutionsHydraulic.Models;

namespace SolutionsHydraulic.Data
{
    public class ApplicationDbContext : DbContext
    {
        public ApplicationDbContext(DbContextOptions<ApplicationDbContext> options) : base(options) { }

        public DbSet<ResidentialUnit> ResidentialUnits { get; set; }
        public DbSet<Contract> Contracts { get; set; }
        public DbSet<WorkTask> WorkTasks { get; set; }

        protected override void OnModelCreating(ModelBuilder modelBuilder)
        {
            base.OnModelCreating(modelBuilder);

            modelBuilder.Entity<ResidentialUnit>()
                .Property(r => r.NIT)
                .IsRequired();

            modelBuilder.Entity<Contract>()
                .HasIndex(c => c.UnitId)
                .IsUnique();

            modelBuilder.Entity<WorkTask>()
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